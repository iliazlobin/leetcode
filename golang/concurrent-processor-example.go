package processor

import (
	"context"
	"fmt"
	"time"

	"github.com/kelseyhightower/envconfig"
	log "github.com/sirupsen/logrus"
)

type Processor struct {
	Config
	bigQuery *bigquery.BigQueryManager
	newRelic *newrelic.NewRelicManager
}

type Config struct {
	Regions        []string `envconfig:"REGIONS" default:"guse4,gnae1,gase1"`
	ServicesLimit  int      `envconfig:"SERVICES_LIMIT" default:"0"`
	DryRun         bool     `envconfig:"DRY_RUN" default:"false"`
	Concurrency    int      `envconfig:"CONCURRENCY" default:"5"`
	WarningsLimit  int      `envconfig:"WARNINGS_LIMIT" default:"0"`
	NewRelicConfig newrelic.Config
	BigQueryConfig bigquery.Config
}

func NewProcessor(c Config) (*Processor, error) {
	var cfg Config
	err := envconfig.Process("processor", &cfg)
	if err != nil {
		return nil, err
	}

	if len(c.Regions) > 0 {
		cfg.Regions = c.Regions
	}
	if c.ServicesLimit > 0 {
		cfg.ServicesLimit = c.ServicesLimit
	}
	if c.DryRun {
		cfg.DryRun = c.DryRun
	}
	if c.Concurrency > 0 {
		cfg.Concurrency = c.Concurrency
	}
	if c.WarningsLimit > 0 {
		cfg.WarningsLimit = c.WarningsLimit
	}

	p := &Processor{
		Config: cfg,
	}

	p.newRelic, err = newrelic.NewManager(cfg.NewRelicConfig)
	if err != nil {
		return nil, err
	}

	p.bigQuery, err = bigquery.NewManager(cfg.BigQueryConfig)
	if err != nil {
		return nil, err
	}

	return p, nil
}

func (p *Processor) retrieveDetails(ctx context.Context, data *core.ServiceData) *RetrieveDetailsOutput {
	service := data.Service

	log.WithFields(log.Fields{
		"namespace": service.Namespace,
		"name":      service.Name,
	}).Tracef("querying service details")

	hpaConfig, err := p.newRelic.QueryHpaConfig(ctx, service)
	if err != nil {
		return &RetrieveDetailsOutput{
			PipelineOutput: PipelineOutput{
				Err: fmt.Errorf("error querying hpa config for %s: %w", service, err),
			},
		}
	}

	var deploymentConfig *core.DeploymentConfig
	deploymentConfig, err = p.newRelic.QueryAggregateDeploymentConfig(ctx, service, "")
	if err != nil {
		return &RetrieveDetailsOutput{
			PipelineOutput: PipelineOutput{
				Err: fmt.Errorf("error querying aggregate deployment config for %s: %w", service, err),
			},
		}
	}

	var deploymentConfig1m *core.DeploymentConfig
	deploymentConfig1m, err = p.newRelic.QueryAggregateDeploymentConfig(ctx, service, "1 MONTH AGO")
	if err != nil {
		return &RetrieveDetailsOutput{
			PipelineOutput: PipelineOutput{
				Err: fmt.Errorf("error querying aggregate deployment config for %s: %w", service, err),
			},
		}
	}

	var cpuUtilization *core.CpuUtilization
	cpuUtilization, err = p.newRelic.QueryUtilization(ctx, service)
	if err != nil {
		return &RetrieveDetailsOutput{
			PipelineOutput: PipelineOutput{
				Err: fmt.Errorf("error querying utilization for %s: %w", service, err),
			},
		}
	}

	var retrievedDetails []*RetrievedDetails

	isHpa := false
	if hpaConfig.DesiredReplicas > 0 {
		isHpa = true
	}

	if !isHpa {
		details := &core.ServiceDetails{
			Service:            service,
			Spec:               data.Spec,
			Spec1M:             data.Spec1M,
			HpaConfig:          hpaConfig,
			DeploymentConfig:   deploymentConfig,
			DeploymentConfig1M: deploymentConfig1m,
			CpuUtilization:     cpuUtilization,
		}
		retrievedDetails = append(retrievedDetails, &RetrievedDetails{
			ServiceSpec:    data.Spec,
			ServiceDetails: details,
		})
	} else {
		for _, region := range p.Regions {
			hpaConfig, err := p.newRelic.QueryRegionSpecificHpaConfig(ctx, service, region, "")
			if err != nil {
				return &RetrieveDetailsOutput{
					PipelineOutput: PipelineOutput{
						Err: fmt.Errorf("error querying region specific configuration %s: %w", service, err),
					},
				}
			}

			if hpaConfig.DesiredReplicas == 0 {
				continue
			}

			hpaConfig1m, err := p.newRelic.QueryRegionSpecificHpaConfig(ctx, service, region, "1 MONTH AGO")
			if err != nil {
				return &RetrieveDetailsOutput{
					PipelineOutput: PipelineOutput{
						Err: fmt.Errorf("error querying region specific configuration %s: %w", service, err),
					},
				}
			}

			cpuUtilization, err := p.newRelic.QueryRegionSpecificUtilization(ctx, service, region)
			if err != nil {
				return &RetrieveDetailsOutput{
					PipelineOutput: PipelineOutput{
						Err: fmt.Errorf("error querying region specific utilization %s: %w", service, err),
					},
				}
			}

			rps, err := p.newRelic.QueryRps(ctx, service, region)
			if err != nil {
				return &RetrieveDetailsOutput{
					PipelineOutput: PipelineOutput{
						Err: fmt.Errorf("error querying istio rps %s: %w", service, err),
					},
				}
			}

			details := &core.HpaServiceDetails{
				Service:        service,
				Spec:           data.Spec,
				Spec1M:         data.Spec1M,
				Region:         region,
				HpaConfig:      hpaConfig,
				HpaConfig1M:    hpaConfig1m,
				CpuUtilization: cpuUtilization,
				IstioRps:       rps,
			}

			retrievedDetails = append(retrievedDetails, &RetrievedDetails{
				ServiceSpec:       data.Spec,
				HpaServiceDetails: details,
			})
		}
	}

	return &RetrieveDetailsOutput{
		RetrievedDetails: retrievedDetails,
	}
}

func (p *Processor) insertData(ctx context.Context, details *RetrievedDetails) *InsertDataResult {
	if details.ServiceDetails != nil {
		log.WithFields(log.Fields{
			"namespace": details.ServiceDetails.Service.Namespace,
			"name":      details.ServiceDetails.Service.Name,
		}).Tracef("inserting service data")

		err := p.bigQuery.Insert(ctx, details.ServiceDetails.Service, details.ServiceDetails)
		if err != nil {
			return &InsertDataResult{
				PipelineOutput: PipelineOutput{
					Err: fmt.Errorf("failed to insert data: %w", err),
				},
				InsertedData: &InsertedData{
					ServiceSpec:      details.ServiceSpec,
					RetrievedDetails: details,
				},
			}
		}
	}

	if details.HpaServiceDetails != nil {
		log.WithFields(log.Fields{
			"namespace": details.HpaServiceDetails.Service.Namespace,
			"name":      details.HpaServiceDetails.Service.Name,
		}).Tracef("inserting hpa service data")

		err := p.bigQuery.HpaInsert(ctx, details.HpaServiceDetails.Service, details.HpaServiceDetails)
		if err != nil {
			return &InsertDataResult{
				PipelineOutput: PipelineOutput{
					Err: fmt.Errorf("failed to insert Hpa data: %w", err),
				},
				InsertedData: &InsertedData{
					ServiceSpec:      details.ServiceSpec,
					RetrievedDetails: details,
				},
			}
		}
	}

	return &InsertDataResult{
		InsertedData: &InsertedData{
			ServiceSpec:      details.ServiceSpec,
			RetrievedDetails: details,
		},
	}
}

func (p *Processor) Run(ctx context.Context) error {
	log.WithFields(log.Fields{
		"limit": p.ServicesLimit,
	}).Debugf("querying service specs")

	serviceData, err := p.newRelic.QueryServiceData(ctx, p.ServicesLimit)
	if err != nil {
		return fmt.Errorf("error querying service specs: %w", err)
	}

	pipeCtx, pipeCancel := context.WithCancel(ctx)

	specCh := pipelineGenerateSpec(pipeCtx, serviceData)
	detailsCh := pipelineRetrieveDetails(pipeCtx, p.Concurrency, specCh, p.retrieveDetails)

	start := time.Now()

	var processingError error
	var serviceDetails []*core.ServiceDetails
	var hpaServiceDetails []*core.HpaServiceDetails
	routines := 0
	warnings := 0
	if p.DryRun {
		log.Infof("start processing %d services (dry run)", len(serviceData))

		for res := range detailsCh {
			if res.Err != nil {
				pipeCancel()
				log.Errorf("processing error (dry run): %s", res.Err)
				processingError = fmt.Errorf("processing error (dry run): %w", res.Err)
				break
			}
			if res.Warn != "" {
				log.Warnf("processing warning (dry run): %s", res.Warn)
				warnings++
				if (p.WarningsLimit > 0) && (warnings >= p.WarningsLimit) {
					pipeCancel()
					log.Warnf("reached warnings limit (%d), stop processing", p.WarningsLimit)
					break
				}
			}
			if res.RetrievedDetails.ServiceDetails != nil {
				serviceDetails = append(serviceDetails, res.RetrievedDetails.ServiceDetails)
			}
			if res.RetrievedDetails.HpaServiceDetails != nil {
				hpaServiceDetails = append(hpaServiceDetails, res.RetrievedDetails.HpaServiceDetails)
			}
			routines++
		}
	} else {
		log.Debugf("start processing %d services", len(serviceData))

		resultCh := pipelineInsertData(pipeCtx, p.Concurrency, detailsCh, p.insertData)
		for res := range resultCh {
			if res.Err != nil {
				pipeCancel()
				log.Error(res.Err)
				processingError = fmt.Errorf("processing error: %w", res.Err)
				break
			}
			if res.Warn != "" {
				log.Warnf("processing warning (dry run): %s", res.Warn)
				warnings++
				if (p.WarningsLimit > 0) && (warnings >= p.WarningsLimit) {
					pipeCancel()
					log.Warnf("reached warnings limit (%d), stop processing", p.WarningsLimit)
					break
				}
			}
			if res.InsertedData.RetrievedDetails.ServiceDetails != nil {
				serviceDetails = append(serviceDetails, res.InsertedData.RetrievedDetails.ServiceDetails)
				log.WithFields(log.Fields{
					"namespace": res.InsertedData.RetrievedDetails.ServiceDetails.Service.Namespace,
					"name":      res.InsertedData.RetrievedDetails.ServiceDetails.Service.Name,
				}).Debugf("service data inserted: %d", len(serviceDetails))
			}
			if res.InsertedData.RetrievedDetails.HpaServiceDetails != nil {
				hpaServiceDetails = append(hpaServiceDetails, res.InsertedData.RetrievedDetails.HpaServiceDetails)
				log.WithFields(log.Fields{
					"namespace": res.InsertedData.RetrievedDetails.HpaServiceDetails.Service.Namespace,
					"name":      res.InsertedData.RetrievedDetails.HpaServiceDetails.Service.Name,
				}).Debugf("hpa service data inserted: %d", len(hpaServiceDetails))
			}
			routines++
		}
	}

	duration := time.Since(start)

	for i, service := range serviceDetails {
		log.WithFields(
			log.Fields{
				"service": service.Service,
				"cpu":     service.CpuUtilization,
			},
		).Tracef("service details: %d/%d", i+1, len(serviceDetails))
	}
	for i, service := range hpaServiceDetails {
		log.WithFields(
			log.Fields{
				"service": service.Service,
				"cpu":     service.CpuUtilization,
				"region":  service.Region,
				"hpa":     service.HpaConfig,
			},
		).Tracef("hpa service details: %d/%d", i+1, len(hpaServiceDetails))
	}

	if processingError != nil {
		pipeCancel()
		log.WithFields(
			log.Fields{
				"concurrency":   p.Concurrency,
				"queryTimeout":  p.NewRelicConfig.QueryTimeout,
				"queryPeriod":   p.NewRelicConfig.QueryPeriod,
				"limit":         p.ServicesLimit,
				"warnings":      warnings,
				"warningsLimit": p.WarningsLimit,
				"routines":      routines,
				"services":      len(serviceData),
				"entries":       len(serviceDetails),
				"hpaEntries":    len(hpaServiceDetails),
			},
		).Errorf("completed in %s with error: %v", duration, processingError)
		return processingError
	}

	log.WithFields(
		log.Fields{
			"concurrency":   p.Concurrency,
			"queryTimeout":  p.NewRelicConfig.QueryTimeout,
			"queryPeriod":   p.NewRelicConfig.QueryPeriod,
			"limit":         p.ServicesLimit,
			"warnings":      warnings,
			"warningsLimit": p.WarningsLimit,
			"routines":      routines,
			"services":      len(serviceData),
			"entries":       len(serviceDetails),
			"hpaEntries":    len(hpaServiceDetails),
		},
	).Infof("completed in %s with %d warnings", duration, warnings)

	if warnings > 0 {
		pipeCancel()
		return fmt.Errorf("warnings limit reached: %d", warnings)
	}

	pipeCancel()
	return nil
}

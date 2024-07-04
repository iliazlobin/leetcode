package gsm

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"regexp"

	secretmanager "cloud.google.com/go/secretmanager/apiv1"
	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
	log "github.com/sirupsen/logrus"
)

var re = regexp.MustCompile("^gsm:([^:]+):([^:]+)$")
var client *secretmanager.Client

func init() {
	var err error
	client, err = secretmanager.NewClient(context.Background())
	if err != nil {
		log.Fatalf("failed to create secretmanager client: %v", err)
	}
}

var NotGsmSpec = errors.New("env is not a gsm spec (gsm:secretName:jsonField)")

func RetrieveSecretFromEnv(projectId, env string) (string, error) {
	match := re.FindSubmatch([]byte(env))
	if match == nil {
		return "", NotGsmSpec
	}

	secretName := string(match[1])
	jsonField := string(match[2])

	log.Debugf("retriving secretName:jsonField: %s:%s", secretName, jsonField)

	ctx := context.Background()

	secretVersion := fmt.Sprintf("projects/%s/secrets/%s/versions/latest", projectId, secretName)
	result, err := client.AccessSecretVersion(ctx, &secretmanagerpb.AccessSecretVersionRequest{Name: secretVersion})
	if err != nil {
		return "", fmt.Errorf("failed to access secret version: %s/%s: %w", projectId, secretName, err)
	}

	var configJson map[string]string
	err = json.Unmarshal(result.Payload.Data, &configJson)
	if err != nil {
		return "", fmt.Errorf("failed to unmarshal secret payload: %w", err)
	}

	return configJson[jsonField], nil
}

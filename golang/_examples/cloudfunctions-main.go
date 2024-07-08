package main

import (
	"os"
	"path/filepath"
	"runtime"
	"strings"

	"github.com/GoogleCloudPlatform/functions-framework-go/funcframework"
	"github.com/joho/godotenv"
	log "github.com/sirupsen/logrus"
)

func main() {
	log.SetFormatter(&log.TextFormatter{
		FullTimestamp: true, CallerPrettyfier: func(f *runtime.Frame) (string, string) {
			return filepath.Base(f.Function), filepath.Base(f.File)
			//return "", filepath.Base(f.File)
		},
	})
	log.SetReportCaller(true)
	log.SetOutput(os.Stdout)
	log.SetLevel(log.InfoLevel)

	err := godotenv.Load()
	if err == nil {
		log.Debug("Environment variables have been loaded from '.env'")
	}

	if logLevel := os.Getenv("LOG_LEVEL"); logLevel != "" {
		logLevel := strings.ToLower(logLevel)

		switch logLevel {
		case "debug":
			log.SetLevel(log.DebugLevel)
		default:
			log.SetLevel(log.InfoLevel)
		}
	}

	if len(os.Args) > 1 && os.Args[1] == "version" {
		log.Infof("Version: %s", os.Getenv("VERSION"))
		return
	}

	port := "8080"
	if envPort := os.Getenv("PORT"); envPort != "" {
		port = envPort
	}

	log.Infof("Starting server on port %s", port)
	if err := funcframework.Start(port); err != nil {
		log.Fatalf("funcframework.Start: %v\n", err)
	}
}

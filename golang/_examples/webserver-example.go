package webserver

import (
	"encoding/json"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
	"github.com/kelseyhightower/envconfig"
	log "github.com/sirupsen/logrus"
)

type Server struct {
	*mux.Router
	storageMgr    storage.StorageManager
	scriptActions script.Actions
	operations    operation.Operations
}

func NewServer() (*Server, error) {
	server := &Server{}
	err := server.Init()
	if err != nil {
		return nil, err
	}
	return server, nil
}

func (s *Server) Init() error {
	var e ServerEnv
	err := envconfig.Process("server", &e)
	if err != nil {
		return err
	}

	if s.storageMgr == nil {
		s.storageMgr, err = storage.NewStorageClient()
		if err != nil {
			return err
		}
	}

	if s.scriptActions == nil {
		s.scriptActions, err = script.NewScriptManager()
		if err != nil {
			return err
		}
	}

	if s.operations == nil {
		s.operations, err = operation.NewOperationController()
		if err != nil {
			return err
		}
	}

	r := mux.NewRouter()
	// get methods
	r.HandleFunc("/api/service/v1/test", s.test).Methods("GET")
	r.HandleFunc("/api/service/v1/check", s.check).Methods("GET")
	// control methods
	r.HandleFunc("/api/service/v1/stop", s.stop).Methods("POST")
	r.HandleFunc("/api/service/v1/start", s.start).Methods("POST")
	r.HandleFunc("/api/service/v1/dosomething", s.dosomething).Methods("POST")
	// database methods
	r.HandleFunc("/api/service/v1/health", s.health).Methods("GET")
	s.Router = r

	return nil
}

func (s *Server) start(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	values := r.URL.Query()
	portValue := values.Get("port") // mandatory

	port := 0
	if portValue != "" {
		port, _ = strconv.Atoi(portValue)
	}
	if port == 0 {
		log.Error("port is not specified")
		output, _ := json.Marshal(map[string]string{
			"operation": "start",
			"error":     "wrong request parameters",
		})
		http.Error(w, string(output), http.StatusBadRequest)
		return
	}
	if port < 1024 {
		log.Error("port from this range cannot be used")
		output, _ := json.Marshal(map[string]string{
			"operation": "start",
			"error":     "port from this range cannot be used",
		})
		http.Error(w, string(output), http.StatusBadRequest)
		return
	}

	// TODO
}

func (s *Server) health(w http.ResponseWriter, r *http.Request) {
	_ = json.NewEncoder(w).Encode(map[string]string{
		"operation": "health",
		"result":    "ok",
	})
}

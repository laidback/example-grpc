PROJECT := grpctest

GRPC_FLAGS := \
	-I. \
	-I/usr/local/include \
	-I$(GOPATH)/src \
	-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis

all: server client gateway

SERVER_FLAGS := \
	--proto_path=./protos \
	--python_out=grpctest/server \
	--grpc_python_out=grpctest/server \

SERVER_GW_FLAGS := \
	--python_out=grpctest/server \
	--grpc_python_out=grpctest/server

server:
	python3 -m grpc_tools.protoc $(SERVER_FLAGS) $(GRPC_FLAGS) protos/*.proto
	python3 -m grpc_tools.protoc $(SERVER_GW_FLAGS) $(GRPC_FLAGS) google/api/annotations.proto
	python3 -m grpc_tools.protoc $(SERVER_GW_FLAGS) $(GRPC_FLAGS) google/api/http.proto

CLIENT_FLAGS := \
	--proto_path=./protos \
	--python_out=grpctest/client \
	--grpc_python_out=grpctest/client

CLIENT_GW_FLAGS := \
	--python_out=grpctest/client \
	--grpc_python_out=grpctest/client

client:
	python3 -m grpc_tools.protoc $(CLIENT_FLAGS) $(GRPC_FLAGS) protos/*.proto
	python3 -m grpc_tools.protoc $(CLIENT_GW_FLAGS) $(GRPC_FLAGS) google/api/annotations.proto
	python3 -m grpc_tools.protoc $(CLIENT_GW_FLAGS) $(GRPC_FLAGS) google/api/http.proto

GATEWAY_SRC_DIR := $(GOPATH)/src/github.com/laidback/grpctest
GATEWAY_GRPC_DIR := $(GATEWAY_SRC_DIR)/gateway
GATEWAY_FLAGS := \
	--proto_path=./protos \
	--go_out=plugins=grpc:$(GATEWAY_GRPC_DIR) \
	--grpc-gateway_out=logtostderr=true:$(GATEWAY_GRPC_DIR) \

gateway_dirs:
	mkdir -p $(GATEWAY_GRPC_DIR)

gateway: gateway_dirs
	cp grpctest/gateway/gateway.go $(GATEWAY_SRC_DIR)
	python3 -m grpc_tools.protoc $(GATEWAY_FLAGS) $(GRPC_FLAGS) protos/*.proto
	go build -o bin/gateway $(GATEWAY_SRC_DIR)/gateway.go

deps:
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
	go get -u github.com/golang/protobuf/protoc-gen-go
	go get -u google.golang.org/grpc

.PHONY: gateway_dirs

# vim: noexpandtab:

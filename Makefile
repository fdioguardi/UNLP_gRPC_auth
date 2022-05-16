.PHONY: clean setup lint
.DEFAULT_GOAL := help

PYTHON := python
LINTER := black

# Run the server
server:
	$(PYTHON) main.py --server

# Run the client
client:
	$(PYTHON) main.py --client

# Prettify the source code
lint:
	$(LINTER) src

# Clean up
clean:
	find . -name "__pycache__" -exec rm -fr {} +
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find src/service/ -maxdepth 1 -type f -not -name '__init__.py' -delete
	$(PYTHON) -m grpc_tools.protoc -Isrc/service/protos --python_out=src/service/ --grpc_python_out=src/service/ src/service/protos/auth.proto
	$(PYTHON) -m grpc_tools.protoc -Isrc/service/protos --python_out=src/service/ --grpc_python_out=src/service/ src/service/protos/info.proto

# Build the project
setup:
	chmod +x ./setup.sh && ./setup.sh

# Show help
help:
	@echo "——————————————————————————————————————————"
	@echo " Usage: make [options]"
	@echo " Options:"
	@echo "   help:  Show this help message and exit."
	@echo "   clean: Clean up the project."
	@echo "   lint:  Prettify the source code."
	@echo "——————————————————————————————————————————"

.PHONY: clean setup lint
.DEFAULT_GOAL := help

PYTHON := .venv/bin/python
LINTER := black

# Prettify the source code
lint:
	$(LINTER) src

# Clean up
clean:
	find . -name "__pycache__" -exec rm -fr {} +
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	rm -f src/service/*.py
	$(PYTHON) -m grpc_tools.protoc -Isrc/service/protos --python_out=src/service/ --grpc_python_out=src/service/ src/service/protos/auth.proto
	$(PYTHON) -m grpc_tools.protoc -Isrc/service/protos --python_out=src/service/ --grpc_python_out=src/service/ src/service/protos/info.proto

# Show help
help:
	@echo "——————————————————————————————————————————"
	@echo " Usage: make [options]"
	@echo " Options:"
	@echo "   help:  Show this help message and exit."
	@echo "   clean: Clean up the project."
	@echo "   lint:  Prettify the source code."
	@echo "   run:   Run the project."
	@echo "——————————————————————————————————————————"

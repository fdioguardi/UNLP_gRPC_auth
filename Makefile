.PHONY: clean setup
.DEFAULT_GOAL := help

PYTHON := .venv/bin/python

# Clean up
clean:
	find . -name "__pycache__" -exec rm -fr {} +
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	rm -f src/service/*.py
	$(PYTHON) -m grpc_tools.protoc -Isrc/service/protos --python_out=src/service/ --grpc_python_out=src/service/ protos/{auth,info}.proto


# Set up the environment
setup:
	python -m venv .venv
	$(PYTHON) -m pip install --upgrade pip
	pip install -r requirements.txt

# Show help
help:
	@echo "——————————————————————————————————————————"
	@echo " Usage: make [options]"
	@echo " Options:"
	@echo "   help:  Show this help message and exit."
	@echo "   clean: Clean up the project."
	@echo "   setup: Set up the environment."
	@echo "   run:   Run the project."
	@echo "——————————————————————————————————————————"

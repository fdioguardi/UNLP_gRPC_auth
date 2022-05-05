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


# Set up the environment
setup:
	yes "" | apt install mongodb
	service mongodb start
	apt install -y build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev zlib1g-dev openssl libffi-dev python3-dev python3-setuptools wget
	mkdir /tmp/Python37
	mkdir /tmp/Python37/Python-3.7.10
	cd /tmp/Python37/
	wget https://www.python.org/ftp/python/3.7.10/Python-3.7.10.tar.xz
	tar xvf Python-3.7.10.tar.xz -C /tmp/Python37
	cd /tmp/Python37/Python-3.7.10/
	./configure --enable-optimizations
	make altinstall
	cd /pdytr
	python3.7 -m venv .venv
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
	@echo "   lint:  Prettify the source code."
	@echo "   run:   Run the project."
	@echo "——————————————————————————————————————————"

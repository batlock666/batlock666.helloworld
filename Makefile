PYTHON_VERSION := 3.9.13
VENV_DIR := venv

PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
FLAKE8 := $(VENV_DIR)/bin/flake8

all: venv

$(VENV_DIR)/bin/activate: requirements.txt
	pyenv local $(PYTHON_VERSION)
	python -m venv $(VENV_DIR)
	$(PIP) install -q -r requirements.txt

venv: $(VENV_DIR)/bin/activate

develop: venv
	$(PIP) install -q -e .

flake8: venv
	$(FLAKE8) || true

test: develop
	$(PYTHON) -m unittest -v

clean:
	rm -rf src/batlock666/__pycache__/
	rm -rf src/batlock666/helloworld/__pycache__/
	rm -rf src/batlock666.helloworld.egg-info/
	rm -rf tests/__pycache__/
	rm -rf $(VENV_DIR)/
	pyenv local --unset

.PHONY: all venv develop test clean

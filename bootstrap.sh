#!/bin/bash

PYTHON_VERSION='3.9.13'
VENV_DIR='venv'

pyenv local "$PYTHON_VERSION"
python -m venv "$VENV_DIR"
"$VENV_DIR"/bin/pip install -r requirements.txt

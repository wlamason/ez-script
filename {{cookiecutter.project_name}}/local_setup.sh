#!/bin/bash

set -x -e

python3 -m venv venv
. venv/bin/activate
python3 -m pip install pip-tools
pip-compile -o requirements.txt pyproject.toml
pip-compile --extra dev -o dev-requirements.txt pyproject.toml
python3 -m pip install -r dev-requirements.txt
echo "{}" >> secrets.json
python3 {{cookiecutter.project_name}}.py --help

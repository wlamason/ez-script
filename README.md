# ez-script
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

Cookiecutter template to quickly stand up a script with linting, testing, logging, configuration, and secrets.

## Install `cookiecutter`

```
python3 -m pip install cookiecutter
```

## Run `cookiecutter`

```
python3 -m cookiecutter gh:wlamason/ez-script
```

## Run `cookiecutter` locally

```
python3 -m cookiecutter path/to/ez-script
```

## `post_gen_project.sh`

Creates a venv:
```
python3 -m venv venv
source venv/bin/activate
```

Installs `pip-tools`:
```
python3 -m pip install pip-tools
```

Generates requirements files:
```
pip-compile -o requirements.txt pyproject.toml
pip-compile --extra dev -o dev-requirements.txt pyproject.toml
```

Installs dev requirements:
```
pip-sync dev-requirements.txt
```

Runs the program:
```
python3 {{cookiecutter.project_name}}.py --help
```

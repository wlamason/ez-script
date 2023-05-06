# {{cookiecutter.project_name}}
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

> {{cookiecutter.project_description}}

## Basic Usage

```
python3 {{cookiecutter.project_name}}.py
```

## Local setup

Run:
```
./local_setup.sh
```

Which will...

Create venv:
```
python3 -m venv venv
. venv/bin/activate
```

Install `pip-tools`:
```
python3 -m pip install pip-tools
```

Generate requirements files:
```
pip-compile -o requirements.txt pyproject.toml
pip-compile --extra dev -o dev-requirements.txt pyproject.toml
```

Install dev requirements:
```
python3 -m pip install -r dev-requirements.txt
```

Run program:
```
python3 {{cookiecutter.project_name}}.py --help
```

## Show your support

Give a ⭐️ if this project helped you!

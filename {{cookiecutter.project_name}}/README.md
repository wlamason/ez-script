# {{cookiecutter.project_name}}
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

> {{cookiecutter.project_description}}

## Basic Usage

```
python3 {{cookiecutter.project_name}}.py
```

## Linting

Run:
```
ruff format
ruff check --fix
ruff check
```

## Testing

```
pytest
```

## Generate new requirements files

```
pip-compile -o requirements.txt pyproject.toml
pip-compile --extra dev -o dev-requirements.txt pyproject.toml
```

## Relevant documentation

- pydantic - https://docs.pydantic.dev/latest/
- pip-tools - https://pip-tools.readthedocs.io/en/latest/
- pytest - https://docs.pytest.org/en/7.3.x/contents.html
- ruff - https://beta.ruff.rs/docs/

## Show your support

Give a ⭐️ if this project helped you!

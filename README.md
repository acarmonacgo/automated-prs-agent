# Automated PRs Agent Placeholder

A small Python petition-signature domain used to validate a pull request review agent.

## Setup

Python 3.12 is required.

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Checks

```sh
ruff check .
pytest
```

# mlops_lab_01

This repository is a small MLOps lab project that demonstrates a simple Python package with automated testing and CI using GitHub Actions.

## What this repository contains

### Source code (`src/`)
- `src/calculator.py`: Implements basic calculator-style functionality.
- `src/__init__.py`: Marks `src` as a Python package/module.

### Tests (`test/`)
This repo includes two test suites to demonstrate different Python testing frameworks:
- `test/test_pytest.py`: Tests written for **pytest**.
- `test/test_unittest.py`: Tests written for Python’s built-in **unittest** framework.
- `test/__init__.py`: Marks `test` as a Python package/module.

## How to run locally

From the repository root:

### Run pytest tests
```bash
python -m pytest -q
```

### Run unittest tests

```bash
python -m unittest -v
```
## GitHub Actions workflows (.github/workflows/)

This repository includes CI workflows that automatically run the test suites on GitHub to validate changes on pushes and pull requests.

`pytest_action.yml`

* Purpose: Run the pytest test suite in CI.
* Typical behavior:
    * Checks out the repository
    * Sets up Python
    * Installs dependencies (if configured in the workflow)
    * Executes `pytest` to run `test/test_pytest.py` (and any other pytest-discoverable tests)

`unittest_action.yml`
* Purpose: Run the unittest test suite in CI.
* Typical behavior:
    * Checks out the repository
    * Sets up Python
    * Installs dependencies (if configured in the workflow)
    * Executes `python -m unittest ...` to run `test/test_unittest.py` (and any other unittest-discoverable tests)
    
## Repository layout (high level)

* `src/` – application/source code
* `test/` – automated tests (pytest + unittest)
* `.github/workflows/` – CI pipelines (GitHub Actions) for running tests
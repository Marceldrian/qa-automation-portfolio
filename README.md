![Tests](https://github.com/Marceldrian/qa-automation-portfolio/actions/workflows/run_tests.yml/badge.svg)

# QA Automation Portfolio

Automated test framework built with Python, Selenium, Pytest, and GitHub Actions CI/CD.

## Tech Stack
- Python 3.11
- Selenium WebDriver
- Pytest + pytest-html
- Page Object Model (POM)
- GitHub Actions CI

## Test Coverage
- Login: 8 tests (including parametrized invalid login scenarios)
- Inventory: 5 tests
- Cart: 5 tests
- Checkout: 5 tests
- Total: 23 automated test cases

## How to Run
```bash
pip install -r requirements.txt
pytest
```
Reports are generated at reports/report.html

![Tests](https://github.com/Marceldrian/qa-automation-portfolio/actions/workflows/run_tests.yml/badge.svg)

# QA Automation Portfolio — UI Test Framework

Automated end-to-end test framework for a web application using Python, Selenium WebDriver, and Pytest. Built as part of a QA Automation Engineer portfolio.

## Tech Stack

- Python 3.11
- Selenium WebDriver
- Pytest + pytest-html
- Page Object Model (POM)
- GitHub Actions CI/CD

## Project Structure

```
qa-automation-portfolio/
├── tests/           # Test files (login, inventory, cart, checkout)
├── pages/           # Page Object classes
├── utils/           # Browser factory and helpers
├── test_data/       # JSON test data
├── reports/         # Auto-generated HTML reports
└── .github/         # GitHub Actions workflow
```

## Test Coverage

| Feature    | Tests | Type              |
|------------|-------|-------------------|
| Login      | 9     | Functional + parametrized negative cases |
| Inventory  | 5     | Functional        |
| Cart       | 5     | Functional        |
| Checkout   | 5     | Functional + validation |
| **Total**  | **23**|                   |

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Marceldrian/qa-automation-portfolio.git
cd qa-automation-portfolio

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests
pytest
```

Test report is generated at `reports/report.html` after each run.

## CI/CD

Tests run automatically on every push to `main` via GitHub Actions.
The pipeline installs dependencies, sets up Chrome, and runs the full test suite.

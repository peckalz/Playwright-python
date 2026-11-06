
# Playwright Python Automation

UI and API automated tests using Python, Pytest and Playwright.

## Tech Stack

- Python 3.11
- Pytest
- Playwright
- pytest-playwright
- Requests
- GitHub Actions

## Project Structure

```text
Playwright-python/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── test_browser.py
│   ├── test_products.py
│   └── test_api.py
├── .github/
│   └── workflows/
│       └── pytest.yml
├── conftest.py
└── requirements.txt
```

## Test Coverage

### UI Tests
- Login with valid and invalid credentials
- Login form validation
- Product management
- Add and remove products from cart
- Cart validation
- Parameterized tests with different users

### API Tests
- GET user
- GET non-existent user
- POST create user
- PUT update user
- PATCH update user
- DELETE user

## Page Object Model

The project uses the Page Object Model (POM) pattern to separate page interactions from test logic.

Implemented page objects:
- LoginPage
- InventoryPage
- CartPage

## Installation

Clone the repository:

```bash
git clone https://github.com/peckalz/Playwright-python.git
cd Playwright-python
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run Tests

Run all tests:

```bash
python -m pytest -v
```

Run UI tests:

```bash
python -m pytest tests/test_browser.py tests/test_products.py -v
```

Run API tests:

```bash
python -m pytest tests/test_api.py -v
```

## CI

GitHub Actions automatically runs the test suite on every push and pull request.

Workflow: `.github/workflows/pytest.yml`

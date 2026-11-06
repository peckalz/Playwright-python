import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import expect
from pathlib import Path


@pytest.fixture
def adult_user():
    return {"name": "Peter",
            "age": 30}

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def logged_in_user(page, login_page, inventory_page):
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    return inventory_page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screenshot_name = f"{item.name}.png"
            page.screenshot(path=str(screenshot_dir / screenshot_name))
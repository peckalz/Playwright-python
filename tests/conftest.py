import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

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
def minor_user():
    return {"name": "John",
            "age": 15}

@pytest.fixture
def user_with_cleanup():
    print("Creating user")
    user_data = {"name": "Peter", "age": 30}
    yield user_data
    print("Deleting user")
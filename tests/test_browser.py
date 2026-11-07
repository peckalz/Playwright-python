import pytest
from playwright.sync_api import expect

def test_open_page(page):
    page.goto("https://saucedemo.com/")

    assert page.title() == "Swag Labs"


def test_login_form_visible(page):
    page.goto("https://saucedemo.com/")

    username = page.get_by_role("textbox", name="Username")
    password = page.get_by_role("textbox", name="Password")

    expect(username).to_be_visible()
    expect(password).to_be_visible()


@pytest.mark.parametrize(
        "username, password, expected_error",[
            ("wrong_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
            ("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
            ("", "", "Epic sadface: Username is required")
        ]
)
def test_login_with_invalid_credentials(page, username, password, expected_error):
    page.goto("https://saucedemo.com/")

    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text(expected_error)).to_be_visible()


def test_successful_login(page, logged_in_inventory):
    expect(page.get_by_text("Products")).to_be_visible()



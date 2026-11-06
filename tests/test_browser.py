import pytest
from playwright.sync_api import expect

def test_open_page(page):
    page.goto("https://saucedemo.com/")

    assert page.title() == "Swag Labs"


def test_login_form_visible(page):
    page.goto("https://saucedemo.com/")

    username = page.get_by_role("textbox", name="Username")
    password = page.get_by_role("textbox", name="Password")

    assert username.is_visible()
    assert password.is_visible()


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


def test_successful_login(page, logged_in_user):
    logged_in_user
    expect(page.get_by_text("Products")).to_be_visible()


def test_unsuccessful_login_with_invalid_credentials(page, login_page):
    login_page.open()
    login_page.login("wrong_user", "wrong_password")

    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()


def test_unsuccessful_login_with_empty_credentials(page, login_page):
    login_page.open()
    login_page.login("", "")

    expect(page.get_by_text("Epic sadface: Username is required")).to_be_visible()

def test_screenshot_example(page):
    page.goto("https://saucedemo.com/")
    assert False
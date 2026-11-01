import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_products_page_visible(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    expect(page.get_by_text("Sauce Labs Bike Light")).to_be_visible()
    expect(page.get_by_text("Sauce Labs Bolt T-Shirt", exact=True)).to_be_visible()


def test_products_sort_by_price_low_to_high(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.get_by_role("combobox").select_option("lohi")

    products = page.locator(".inventory_item_name")
    first_product = products.first
    last_product = products.last
    expect(first_product).to_have_text("Sauce Labs Onesie")
    expect(last_product).to_have_text("Sauce Labs Fleece Jacket")


def test_add_product_to_cart(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    backpack = page.locator(".inventory_item_description").filter(has_text="Sauce Labs Backpack")
    backpack.get_by_role("button", name="Add to cart").click()
    expect(backpack.get_by_role("button", name="Remove")).to_be_visible()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

def test_remove_product_from_cart(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    backpack = page.locator(".inventory_item_description").filter(has_text="Sauce Labs Backpack")
    backpack.get_by_role("button", name="Add to cart").click()
    expect(backpack.get_by_role("button", name="Remove")).to_be_visible()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    backpack.get_by_role("button", name="Remove").click()
    expect(page.locator(".shopping_cart_badge")).to_be_hidden()


def test_product_visible_in_cart(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    backpack = page.locator(".inventory_item_description").filter(has_text="Sauce Labs Backpack")
    backpack.get_by_role("button", name="Add to cart").click()
    expect(backpack.get_by_role("button", name="Remove")).to_be_visible()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1") 
    page.locator(".shopping_cart_container").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()


def test_checkout_successful(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    backpack = page.locator(".inventory_item_description").filter(has_text="Sauce Labs Backpack")
    backpack.get_by_role("button", name="Add to cart").click()
    expect(backpack.get_by_role("button", name="Remove")).to_be_visible()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1") 
    page.locator(".shopping_cart_container").click()

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    page.get_by_role("button", name="Checkout").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    page.get_by_role("textbox", name="First Name").fill("John")
    page.get_by_role("textbox", name="Last Name").fill("Wick")
    page.get_by_role("textbox", name="Zip/Postal Code").fill("1234")
    page.get_by_role("button", name="Continue").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    page.get_by_role("button", name="Finish").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    
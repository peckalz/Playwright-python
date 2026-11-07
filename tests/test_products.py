from playwright.sync_api import expect

def test_products_page_visible(page, logged_in_inventory):
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    expect(page.get_by_text("Sauce Labs Bike Light")).to_be_visible()
    expect(page.get_by_text("Sauce Labs Bolt T-Shirt", exact=True)).to_be_visible()


def test_products_sort_by_price_low_to_high(page, logged_in_inventory):
    page.get_by_role("combobox").select_option("lohi")

    products = page.locator(".inventory_item_name")
    first_product = products.first
    last_product = products.last
    expect(first_product).to_have_text("Sauce Labs Onesie")
    expect(last_product).to_have_text("Sauce Labs Fleece Jacket")


def test_add_product_to_cart(page, logged_in_inventory):
    logged_in_inventory.add_product_to_cart("Sauce Labs Backpack")
    expect(page.get_by_role("button", name="Remove")).to_be_visible()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

def test_remove_product_from_cart(page, logged_in_inventory):

    logged_in_inventory.add_product_to_cart("Sauce Labs Backpack")
    expect(page.get_by_role("button", name="Remove")).to_be_visible()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    logged_in_inventory.remove_product_from_cart("Sauce Labs Backpack")
    expect(page.locator(".shopping_cart_badge")).to_be_hidden()


def test_product_visible_in_cart(page, logged_in_inventory, cart_page):
    logged_in_inventory.add_product_to_cart("Sauce Labs Backpack")

    expect(page.get_by_role("button", name="Remove")).to_be_visible()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1") 
    cart_page.open()
    cart_page.is_open()
    cart_page.has_product("Sauce Labs Backpack")


def test_checkout_successful(page, logged_in_inventory, cart_page):
    logged_in_inventory.add_product_to_cart("Sauce Labs Backpack")
    expect(page.get_by_role("button", name="Remove")).to_be_visible()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    cart_page.open() 
    cart_page.is_open()
    cart_page.has_product("Sauce Labs Backpack")
    cart_page.checkout()

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
    
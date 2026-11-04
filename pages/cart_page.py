from playwright.sync_api import expect

class CartPage:
    def __init__(self,page):
        self.page = page


    def open(self):
        self.page.locator(".shopping_cart_container").click()


    def is_open(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")


    def has_product(self, product_name):
        expect(self.page.get_by_text(product_name)).to_be_visible()


    def checkout(self):
        self.page.get_by_role("button", name="Checkout").click()
from playwright.sync_api import expect


class InventoryPage:
    def __init__(self, page):
        self.page = page


    def is_open(self):
        expect(self.page.get_by_text("Products")).to_be_visible()


    def add_product_to_cart(self, product_name):
        product = self.page.locator(".inventory_item_description").filter(has_text=product_name)
        product.get_by_role("button", name="Add to cart").click()


    def remove_product_from_cart(self, product_name):
        product = self.page.locator(".inventory_item_description").filter(has_text=product_name)
        product.get_by_role("button", name="Remove").click()
class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

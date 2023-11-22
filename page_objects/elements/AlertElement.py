from selenium.webdriver.common.by import By


class AlertElement:
    THIS = (By.CSS_SELECTOR, ".alert-success")
    COMPARISON = (By.LINK_TEXT, "product comparison")
    LOGIN = (By.LINK_TEXT, "login")
    CART = (By.LINK_TEXT, "shopping cart")

    def __init__(self, driver):
        self.driver = driver
        self.this = self.driver.find_element(*self.THIS)

    @property
    def comparison(self):
        return self.this.find_element(*self.COMPARISON)

    @property
    def login(self):
        return self.this.find_element(*self.LOGIN)

    @property
    def cart(self):
        return self.this.find_element(*self.CART)
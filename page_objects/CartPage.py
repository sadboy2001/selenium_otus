from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CartPage(BasePage):
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")
    FORM_REGISTER = (By.CSS_SELECTOR, "#form-register")
    LOGIN_HREF = (By.CSS_SELECTOR, "a")

    def click_checkout(self):
        self.click(self.element(self.CHECKOUT_LINK))

    def go_to_logging(self):
        self.click(self.element_in_element(self.FORM_REGISTER, self.LOGIN_HREF))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    # BUTTONS = (By.CSS_SELECTOR, ".buttons")
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_LINK).click()

    def verify_product_item(self, product_name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
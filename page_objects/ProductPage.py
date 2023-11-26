import time
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage

class ProductPage(BasePage):
    CART = (By.CSS_SELECTOR, "#button-cart")

    def add_to_cart(self):
        time.sleep(1.5)
        self.click(self.element(self.CART))
        time.sleep(1)

    def product_info(self):
        return self.driver.find_element(By.TAG_NAME, "h1").get_attribute("innerHTML")
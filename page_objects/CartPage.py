from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.BasePage import BasePage


class CartPage(BasePage):
    # BUTTONS = (By.CSS_SELECTOR, ".buttons")
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")

    def click_checkout(self):
        self.click(self.element(self.CHECKOUT_LINK))
        # self.driver.find_element(*self.CHECKOUT_LINK).click()

    def verify_product_item(self, product_name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
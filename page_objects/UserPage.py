from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.BasePage import BasePage


class UserPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button")
    WISH_LIST_LINK = (By.LINK_TEXT, 'Wish List')
    PAYMENT_FORM = ((By.ID, "payment-new"))
    FORM_LOGIN = (By.ID, "form-login")

    def login(self, username, password):
        self.driver.find_element(*self.FORM_LOGIN).find_element(*self.EMAIL_INPUT).send_keys(username)
        self.driver.find_element(*self.FORM_LOGIN).find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.FORM_LOGIN).find_element(*self.LOGIN_BUTTON).click()

    def open_wish_list(self):
        self.driver.find_element(*self.WISH_LIST_LINK).click()

    def verify_payment_form(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PAYMENT_FORM))

    def verify_product_item(self, product_name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
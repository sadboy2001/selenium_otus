from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class RegisterPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    AGREE = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#form-register > div.text-end button")

    def register(self, first_name, last_name, email, password):
        self._input(self.element(self.FIRST_NAME), first_name)
        self._input(self.element(self.LAST_NAME), last_name)
        self._input(self.element(self.EMAIL), email)
        self._input(self.element(self.PASSWORD), password)
        self.logger.info("Click 'AGREE'")
        self.click(self.element(self.AGREE))
        self.logger.info("Click 'CONTINUE'")
        self.click(self.element(self.CONTINUE_BUTTON))

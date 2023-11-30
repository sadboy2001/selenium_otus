from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class UserPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button")
    FORM_LOGIN = (By.ID, "form-login")

    def login(self, username, password):
        self._input(
            self.element_in_element(self.FORM_LOGIN, self.EMAIL_INPUT), username
        )
        self._input(
            self.element_in_element(self.FORM_LOGIN, self.PASSWORD_INPUT), password
        )
        self.logger.info("Click 'LOGIN'")
        self.click(self.element_in_element(self.FORM_LOGIN, self.LOGIN_BUTTON))

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button")
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    HEADER = (By.CSS_SELECTOR, "#content > div.page-header .float-end")
    NEW_NAME = (By.CSS_SELECTOR, "#input-name-1")
    NEW_META = (By.CSS_SELECTOR, "#input-meta-title-1")
    NAVIGATION = (By.CSS_SELECTOR, "#navigation")


    def login(self, username, password):
        self.logger.info("Input 'USERNAME'")
        self._input(self.element(self.EMAIL_INPUT), username)
        # EMAIL_INPUT
        self.logger.info("Input 'PASSWORD'")
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.logger.info("Click 'LOGIN_BUTTON'")
        self.click(self.element(self.LOGIN_BUTTON))
        return self


    def new_product(self):
        self.logger.info("Click 'CATALOG'")
        click_catalog = self.driver.find_element(*self.CATALOG)
        click_catalog.click()
        time.sleep(2)
        click_catalog.find_elements(By.TAG_NAME, "li")[1].click()

    def load_page(self):
        self.logger.info("Wait 'PAGE'")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.NAVIGATION))

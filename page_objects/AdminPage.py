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
    HEADER = (By.CSS_SELECTOR, "#content > div.page-header .container-fluid")


    def login(self, username, password):
        self._input(self.element(self.EMAIL_INPUT), username)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys(username)
        # self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        # self.driver.find_element(*self.LOGIN_BUTTON).click()


    def new_product(self):
        click_catalog = self.driver.find_element(*self.CATALOG)
        click_catalog.click()
        time.sleep(1)
        click_catalog.find_elements(By.TAG_NAME, "li")[1].click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "[data-original-title='Add New']").click()
        get_header = self.driver.find_elements(*self.HEADER)[0]
        time.sleep(2)
        get_header.click()
        time.sleep(3)
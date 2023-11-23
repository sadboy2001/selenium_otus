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
        time.sleep(2)
        click_catalog.find_elements(By.TAG_NAME, "li")[1].click()
        # get_header = self.driver.find_element(*self.HEADER)
        # get_header.find_elements(By.TAG_NAME, "a")[0].click()
        # self._input(self.element(self.NEW_NAME), name)
        # self._input(self.element(self.NEW_META), meta)
        # time.sleep(2)
        # get_header = self.driver.find_element(*self.HEADER)
        # get_header.find_elements(By.TAG_NAME, "button")[0].click()
        # time.sleep(2)

    def load_page(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.NAVIGATION))

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class AdminProductPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "#content > div.page-header .float-end")
    NEW_NAME = (By.CSS_SELECTOR, "#input-name-1")
    NEW_META = (By.CSS_SELECTOR, "#input-meta-title-1")
    NEW_SEO = (By.LINK_TEXT, "SEO")
    NEW_DATA = (By.LINK_TEXT, "Data")
    CHOOSE_ELEMENT = (By.CSS_SELECTOR, "tbody tr")
    BUTTON = (By.CSS_SELECTOR, "button")

    def add_product(self, name, meta):
        get_header = self.driver.find_element(*self.HEADER)
        get_header.find_elements(By.TAG_NAME, "a")[0].click()
        self._input(self.element(self.NEW_NAME), name)
        self._input(self.element(self.NEW_META), meta)
        self.click(self.element(self.NEW_DATA))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-model")))
        self.driver.find_element(By.CSS_SELECTOR, "#input-model").send_keys(meta)
        self.click(self.element(self.NEW_SEO))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-keyword-0-1")))
        self.driver.find_element(By.CSS_SELECTOR, "#input-keyword-0-1").send_keys(name)
        get_header = self.driver.find_element(*self.HEADER)
        get_header.find_elements(*self.BUTTON)[0].click()

    def delete_last_added_product(self):
        self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.CONTROL + Keys.END)
        self.driver.find_element(By.LINK_TEXT, ">|").click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CHOOSE_ELEMENT))
        tb = self.driver.find_element(*self.CHOOSE_ELEMENT)
        tr = tb.find_element(By.CSS_SELECTOR, "td > input")
        tr.click()
        get_header = self.driver.find_element(*self.HEADER)
        get_header.find_elements(By.TAG_NAME, "button")[2].click()

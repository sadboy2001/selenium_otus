import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from page_objects.BasePage import BasePage

filename = "123.png"
class ProductPage(BasePage):
    CART = (By.CSS_SELECTOR, "#button-cart")
    CHECKBOX_1 = (By.CSS_SELECTOR, "#input-option-value-8")
    CHECKBOX_2 = (By.CSS_SELECTOR, "#input-option-value-9")
    CHECKBOX_3 = (By.CSS_SELECTOR, "#input-option-value-10")
    RADIO_SMALL = (By.CSS_SELECTOR, "#input-option-value-5")
    RADIO_MEDIUM = (By.CSS_SELECTOR, "#input-option-value-6")
    RADIO_LARGE = (By.CSS_SELECTOR, "#input-option-value-7")
    TEXTAREA = (By.CSS_SELECTOR, "#input-option-209")
    SELECT = (By.CSS_SELECTOR, "#input-option-217")
    SELECT_FOR_CANON = (By.CSS_SELECTOR, "#input-option-226")
    INPUT_FILE = (By.CSS_SELECTOR, "#input-option-222")

    def add_to_cart(self):
        time.sleep(1.5)
        self.logger.info("Click 'ADD TO CART'")
        self.click(self.element(self.CART))
        time.sleep(1)

    def upload_file(self):
        self.driver.execute_script("arguments[0].type = 'visible';", By.CSS_SELECTOR, "#input-option-222")
        self.element(self.INPUT_FILE)
        # self.actions.send_keys(input_file, filename).perform()


    def _select_canon(self, choose_select):
        self.click(self.element(self.SELECT_FOR_CANON))
        solutions_dropdown = self.element(self.SELECT_FOR_CANON)
        select = Select(solutions_dropdown)
        if choose_select == "red":
            select.select_by_value("15")
        elif choose_select == "blue":
            select.select_by_value("16")
        self.click(self.element(self.SELECT_FOR_CANON))

    def _select(self, choose_select):
        self.click(self.element(self.SELECT))
        solutions_dropdown = self.element(self.SELECT)
        select = Select(solutions_dropdown)
        if choose_select == "red":
            select.select_by_value("4")
        elif choose_select == "blue":
            select.select_by_value("3")
        elif choose_select == "green":
            select.select_by_value("1")
        self.click(self.element(self.SELECT))


    def add_radio(self, choose_radio):
        self.logger.info("Click 'RADIO'")
        if choose_radio == "small":
            self.click(self.element(self.RADIO_SMALL))
        elif choose_radio == "medium":
            self.click(self.element(self.RADIO_MEDIUM))
        elif choose_radio == "large":
            self.click(self.element(self.RADIO_LARGE))

    def click_checkbox(self, choose_checkbox):
        self.logger.info("Click 'ADD CHECKBOX'")
        if choose_checkbox == "checkbox_1":
            self.click(self.element(self.CHECKBOX_1))
        elif choose_checkbox == "checkbox_2":
            self.click(self.element(self.CHECKBOX_2))
        elif choose_checkbox == "checkbox_3":
            self.click(self.element(self.CHECKBOX_3))

    def text_area(self, text):
        self.logger.info("Click 'INPUT TEXT AREA'")
        self._input(self.element(self.TEXTAREA), text)

    def product_info(self):
        return self.driver.find_element(By.TAG_NAME, "h1").get_attribute("innerHTML")
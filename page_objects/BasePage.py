from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.actions = ActionChains(driver)
        self.logger = driver.logger
        self.class_name = type(self).__name__

    @allure.step
    def click(self, element):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, str(element)))
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step
    def _input(self, element, value):
        self.logger.debug("%s: Input %s in input %s" % (self.class_name, value, element))
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element(self, locator: tuple):
        try:
            self.logger.debug("%s: Check if element %s is present" % (self.class_name, str(locator)))
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                name="screenshot",
                body=self.driver.get_screenshot_as_png()
            )
            raise AssertionError(f"No element in vision {locator}")

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element(parent_locator).find_element(*child_locator)

    def elements(self, locator: tuple):
        try:
            self.logger.debug("%s: Check if elements %s is present" % (self.class_name, str(locator)))
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"No element in vision {locator}")

    @allure.step
    def verify_product_item(self, product_name):
        return self.element((By.LINK_TEXT, product_name))
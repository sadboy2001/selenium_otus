from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class MainPage(BasePage):
    FEATURED_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-thumb")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".description h4 a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".description > .price span")
    CAROUSEL_ITEM = (By.CSS_SELECTOR, "#carousel-banner-0")
    HEADER = (By.CSS_SELECTOR, "#top")
    MONEY_LIST = (By.CSS_SELECTOR, "#top > div.row .product-thumb")
    REGISTER = (By.LINK_TEXT, "Register")
    LOGIN = (By.LINK_TEXT, "Login")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    SEARCH_FIELD = (By.CSS_SELECTOR, "[name=search]")

    def click_search(self, text):
        self.logger.info("Input text on 'SEARCH_FIELD'")
        self._input(self.element(self.SEARCH_FIELD), text)
        self.logger.info("Click 'SEARCH'")
        self.click(self.element(self.SEARCH_BUTTON))
        self.driver.find_element(value="content")

    def click_featured_product(self, index):
        feature_product = self.driver.find_elements(*self.FEATURED_PRODUCT)[index]
        product_name = feature_product.find_element(*self.PRODUCT_NAME).text
        self.logger.info("Click on image product")
        feature_product.find_element(By.CSS_SELECTOR, ".image").click()
        return product_name

    def click_carousel(self):
        self.logger.info("Click on image in Main page")
        self.driver.find_element(*self.CAROUSEL_ITEM).click()

    def current_money(self):
        money = (
            self.driver.find_element(*self.HEADER)
            .find_element(By.TAG_NAME, "strong")
            .text
        )
        return money

    def click_money(self, index):
        form_currency = self.driver.find_element(By.CSS_SELECTOR, "#form-currency")
        self.logger.info("Click 'MENU'")
        form_currency.click()
        temp_money = form_currency.find_elements(By.TAG_NAME, "li")[index]
        self.logger.info("Choose element")
        temp_money.click()

    def navigation(self, index):
        form_nav = self.driver.find_element(
            By.CSS_SELECTOR, "#top > div.container .nav.float-end"
        )
        temp_money = form_nav.find_elements(By.TAG_NAME, "li")[index]
        temp_money.click()

    def register_login(self, index):
        if index == 0:
            self.click(self.element(self.REGISTER))
        elif index == 1:
            self.click(self.element(self.LOGIN))

    def check_description(self, index):
        feature_product = self.driver.find_elements(*self.FEATURED_PRODUCT)[index]
        return feature_product.find_element(*self.PRODUCT_PRICE).text

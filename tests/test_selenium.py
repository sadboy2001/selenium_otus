import time

import allure
import pytest

from selenium.webdriver.common.alert import Alert

from page_objects.MainPage import MainPage
from page_objects.UserPage import UserPage
from page_objects.ProductPage import ProductPage
from page_objects.CartPage import CartPage
from page_objects.AdminPage import AdminPage
from page_objects.RegisterPage import RegisterPage
from page_objects.elements.AlertElement import AlertElement
from page_objects.AdminProductPage import AdminProductPage

@allure.feature('Search')
@allure.title('Check search')
@pytest.mark.parametrize('search', ['test', 'iphone', 'iMac'])
def test_search_input(driver, search):
    MainPage(driver).click_search(search)

@allure.feature('Product')
@allure.story('Check info')
@allure.title('Check description after main page')
def test_input(driver):
    MainPage(driver).click_carousel()
    assert ProductPage(driver).product_info() == "Samsung Galaxy Tab 10.1"

@allure.feature('Bottom menu')
@allure.story('Check Apple')
@allure.title('Check apple product after main page')
def test_bottom(driver):
    MainPage(driver).check_bottom()


@allure.feature('Product')
@allure.story('Check info')
@allure.title('Check description after main page')
def test_input_negative(driver):
    with pytest.raises(Exception):
        MainPage(driver).click_carousel()
        assert ProductPage(driver).product_info() == "Samsung Galaxy Tab 10"

@allure.feature('Register')
@allure.title('Check registration')
@pytest.mark.parametrize('first_name, last_name, email, password',
                         [
                             ('IvanIvanich', 'Ivanich', 'Ivanich@gmail.com', 'test1'),
                             ('Fedya', 'Alekseivic', 'F.Aleks@ya.ru', 'test2'),
                             ('Sasha', 'Horus', 'hrw@mail.ru', 'test3'),

                         ])
def test_login_admin(driver, first_name, last_name, email, password):
    MainPage(driver).navigation(1)
    MainPage(driver).register_login(0)
    RegisterPage(driver).register(first_name, last_name, email, password)

@allure.feature('Menu')
@allure.story('Click on menu')
@allure.title('Change money in menu')
@pytest.mark.parametrize('money', [0, 1])
def test_money(driver, money):
    old_money = MainPage(driver).current_money()
    MainPage(driver).click_money(money)
    assert old_money != MainPage(driver).current_money()


@allure.feature('Product')
@allure.story('Check info')
@allure.title('Change money in description')
@pytest.mark.parametrize('id', [0, 1])
def test_value(driver, id):
    old_value = MainPage(driver).check_description(id)
    MainPage(driver).click_money(id)
    assert old_value != MainPage(driver).check_description(id)


# @allure.feature('Shopping Cart')
# @allure.story('Add product to cart')
# @allure.title('Adding single product to cart')
# @pytest.mark.parametrize('select, choose_radio, choose_checkbox',
#                          [
#                              ('red', 'small', 'checkbox_1'),
#                              ('blue', 'medium', 'checkbox_3'),
#                              ('green', 'large', 'checkbox_2'),
#                              ('red', 'large', 'checkbox_2'),
#                              ('blue', 'medium', 'checkbox_1'),
#                              ('green', 'small', 'checkbox_3'),
#                              ('red', 'small', 'checkbox_3'),
#                              ('blue', 'large', 'checkbox_1'),
#                              ('green', 'medium', 'checkbox_2'),
#
#                          ])
# def test_add_to_cart(driver, choose_radio, choose_checkbox, select):
#     product_name = MainPage(driver).click_featured_product(1)
#     ProductPage(driver).add_radio(choose_radio)
#     ProductPage(driver).click_checkbox(choose_checkbox)
#     ProductPage(driver)._select(select)
#     ProductPage(driver).text_area("test")
#     ProductPage(driver).upload_file()
#     ProductPage(driver).add_to_cart()
#     AlertElement(driver).cart.click()
#     CartPage(driver).verify_product_item(product_name)
#     CartPage(driver).click_checkout()
#     CartPage(driver).go_to_logging()
#     UserPage(driver).login("test1@mail.ru", "test1")

def test_add_iphone(driver):
    product_name = MainPage(driver).click_featured_product(0)
    ProductPage(driver).add_to_cart()
    AlertElement(driver).cart.click()
    CartPage(driver).verify_product_item(product_name)
    CartPage(driver).click_checkout()
    CartPage(driver).go_to_logging()
    UserPage(driver).login("test1@mail.ru", "test1")

@pytest.mark.parametrize('select_options',["red","blue"])
def test_add_canon(driver, select_options):
    product_name = MainPage(driver).click_featured_product(2)
    ProductPage(driver)._select_canon(select_options)
    ProductPage(driver).add_to_cart()
    AlertElement(driver).cart.click()
    CartPage(driver).verify_product_item(product_name)
    CartPage(driver).click_checkout()
    CartPage(driver).go_to_logging()
    UserPage(driver).login("test1@mail.ru", "test1")


@allure.feature('Admin')
@allure.title('Login as Admin')
def test_admin(driver):
    driver.get("http:/localhost/administration/")
    AdminPage(driver).login("user", "bitnami")
    driver.find_element(value="content")
    AdminPage(driver).load_page()

@allure.feature('Admin')
@allure.title('Login as Admin')
def test_admin_negative(driver):
    with pytest.raises(Exception):
        driver.get("http:/localhost/administration/")
        AdminPage(driver).login("bitnami", "user")
        driver.find_element(value="content")
        AdminPage(driver).load_page()

@allure.feature('Admin')
@allure.story('Add product to catalog')
@allure.title('Adding single product to catalog')
def test_new_product(driver):
    driver.get("http:/localhost/administration/")
    AdminPage(driver).login("user", "bitnami")
    AdminPage(driver).load_page()
    AdminPage(driver).new_product()
    AdminProductPage(driver).add_product("testnew", "testnew")
    time.sleep(3)
    AlertElement(driver)

@allure.feature('Admin')
@allure.story('Delete product from catalog')
@allure.title('Delete single product from catalog')
def test_delete_product(driver):
    driver.get("http:/localhost/administration/")
    AdminPage(driver).login("user", "bitnami")
    AdminPage(driver).load_page()
    AdminPage(driver).new_product()
    AdminProductPage(driver).delete_last_added_product()
    Alert(driver).accept()

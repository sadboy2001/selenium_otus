import allure

from selenium.webdriver.common.alert import Alert

from page_objects.MainPage import MainPage
from page_objects.UserPage import UserPage
from page_objects.ProductPage import ProductPage
from page_objects.CartPage import CartPage
from page_objects.AdminPage import AdminPage
from page_objects.RegisterPage import RegisterPage
from page_objects.elements.AlertElement import AlertElement
from page_objects.AdminProductPage import AdminProductPage


@allure.feature("Search")
@allure.title("Check search")
def test_search_input(driver):
    MainPage(driver).click_search("test")


@allure.feature("Product")
@allure.story("Check info")
@allure.title("Check description after main page")
def test_input(driver):
    MainPage(driver).click_carousel()
    assert ProductPage(driver).product_info() == "Samsung Galaxy Tab 10.1"


@allure.feature("Register")
@allure.title("Check registration")
def test_login_admin(driver):
    MainPage(driver).navigation(1)
    MainPage(driver).register_login(0)
    RegisterPage(driver).register("first_name", "user_test", "test1@mail.ru", "test1")


@allure.feature("Menu")
@allure.story("Click on menu")
@allure.title("Change money in menu")
def test_money(driver):
    old_money = MainPage(driver).current_money()
    MainPage(driver).click_money(1)
    assert old_money != MainPage(driver).current_money()


@allure.feature("Product")
@allure.story("Check info")
@allure.title("Change money in description")
def test_value(driver):
    old_value = MainPage(driver).check_description(1)
    MainPage(driver).click_money(1)
    assert old_value != MainPage(driver).check_description(1)


@allure.feature("Shopping Cart")
@allure.story("Add product to cart")
@allure.title("Adding single product to cart")
def test_add_to_cart(driver):
    product_name = MainPage(driver).click_featured_product(1)
    ProductPage(driver).add_to_cart()
    AlertElement(driver).cart.click()
    CartPage(driver).verify_product_item(product_name)
    CartPage(driver).click_checkout()
    CartPage(driver).go_to_logging()
    UserPage(driver).login("test1@mail.ru", "test1")


@allure.feature("Admin")
@allure.title("Login as Admin")
def test_admin(driver):
    driver.get("http:/localhost/administration/")
    AdminPage(driver).login("user", "bitnami")
    driver.find_element(value="content")


@allure.feature("Admin")
@allure.story("Add product to catalog")
@allure.title("Adding single product to catalog")
def test_new_product(driver):
    driver.get("http:/localhost/administration/")
    AdminPage(driver).login("user", "bitnami")
    AdminPage(driver).load_page()
    AdminPage(driver).new_product()
    AdminProductPage(driver).add_product("testnew", "testnew")
    AlertElement(driver)


@allure.feature("Admin")
@allure.story("Delete product from catalog")
@allure.title("Delete single product from catalog")
def test_delete_product(driver):
    driver.get("http:/localhost/administration/")
    AdminPage(driver).login("user", "bitnami")
    AdminPage(driver).load_page()
    AdminPage(driver).new_product()
    AdminProductPage(driver).delete_last_added_product()
    Alert(driver).accept()

import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from page_objects.MainPage import MainPage
from page_objects.UserPage import UserPage
from page_objects.ProductPage import ProductPage
from page_objects.CartPage import CartPage
from page_objects.AdminPage import AdminPage
from page_objects.RegisterPage import RegisterPage
from page_objects.elements.AlertElement import AlertElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_input(driver, base_url):
    # driver.get(base_url)
    driver.find_element(By.NAME, "search").send_keys("test")
    driver.find_element(By.CSS_SELECTOR, "#search button").click()
    driver.find_element(value="content")

def test_input(driver):
    # driver.get(base_url)
    MainPage(driver).click_carousel()
    # product_name = MainPage(driver).click_featured_product(1)
    assert driver.find_element(By.XPATH, "//h2[contains(text(),'Tablets')]").text == "Tablets"


def test_login_admin(driver):
    # driver.get(base_url)
    # driver.find_element(By.XPATH, "//body/nav[@id='top']/div[1]/div[2]/ul[1]/li[2]/div[1]/a[1]").click()
    # driver.find_element(By.LINK_TEXT, "Register").click()
    MainPage(driver).navigation(1)
    MainPage(driver).register_login(0)
    RegisterPage(driver).register("first_name", "user_test", "test1@mail.ru", "test1")
    # driver.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys("test_user")
    # driver.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys("user_test")
    # driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys("test1@mail.ru")
    # driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys("test1")
    # driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]").click()

def test_money(driver):
    # driver.get(base_url)
    # old_money = driver.find_element(By.TAG_NAME, "strong").text
    old_money = MainPage(driver).current_money()
    time.sleep(2)
    MainPage(driver).click_money(1)
    time.sleep(2)
    assert old_money != MainPage(driver).current_money()
    # driver.find_element(By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[1]/form[1]/div[1]/a[1]").click()
    # driver.find_element(By.LINK_TEXT, "€ Euro").click()
    # assert driver.find_element(By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[1]/form[1]/div[1]/a[1]").text != old_money


def test_value(driver):
    # driver.get(base_url)
    old_value = MainPage(driver).check_description(1)
    MainPage(driver).click_money(1)
    assert old_value != MainPage(driver).check_description(1)
    # old_value = driver.find_element(By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").text
    # driver.find_element(By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[1]/form[1]/div[1]/a[1]").click()
    # driver.find_element(By.LINK_TEXT, "€ Euro").click()
    # assert driver.find_element(By.XPATH,"//body/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").text != old_value


def test_add_to_cart(driver):
    # driver.get(base_url)
    product_name = MainPage(driver).click_featured_product(1)
    # feature_product = driver.find_elements(By.CSS_SELECTOR, "#content > div.row .product-thumb")[0]
    # product_name = feature_product.find_element(By.CSS_SELECTOR, ".description h4 a").text
    # feature_product.find_element(By.CSS_SELECTOR, ".image").click()
    ProductPage(driver).add_to_cart()
    # driver.find_element(By.CSS_SELECTOR, "#button-cart").click()
    # time.sleep(1)
    AlertElement(driver).cart.click()
    # driver.find_element(By.CSS_SELECTOR, ".alert-success").find_element(By.LINK_TEXT, "shopping cart").click()
    CartPage(driver).verify_product_item(product_name)
    CartPage(driver).click_checkout()
    # WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    # driver.find_element(By.LINK_TEXT, "Checkout").click()
    driver.find_element(By.CSS_SELECTOR, "#form-register").find_element(By.CSS_SELECTOR, "a").click()
    UserPage(driver).login("test1@mail.ru", "test1")
    # form_login = driver.find_element(By.ID, "form-login")
    # form_login.find_element(By.CSS_SELECTOR, "#input-email").send_keys("test1@mail.ru")
    # form_login.find_element(By.CSS_SELECTOR, "#input-password").send_keys("test1")
    # form_login.find_element(By.CSS_SELECTOR, "button").click()

def test_admin(driver):
    driver.get("http:/localhost/administration/")
    # driver.get(base_url + "/administration/")
    AdminPage(driver).login("user", "bitnami")
    # driver.find_element(By.CSS_SELECTOR, "#input-username").send_keys("user")
    # driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys("bitnami")
    # driver.find_element(By.CSS_SELECTOR, "button").click()
    driver.find_element(value="content")


def test_new_product(driver):
    driver.get("http:/localhost/administration/")
    AdminPage(driver).login("user", "bitnami")
    time.sleep(2)
    AdminPage(driver).new_product()
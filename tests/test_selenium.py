import time

from selenium.webdriver.common.by import By


def test_search_input(driver, base_url):
    driver.get(base_url)
    driver.find_element(By.NAME, "search").send_keys("test")
    driver.find_element(By.CSS_SELECTOR, "#search button").click()
    driver.find_element(value="content")

def test_input(driver, base_url):
    driver.get(base_url)
    driver.find_element(By.XPATH, "//body/main[1]/div[1]/nav[1]/div[2]/ul[1]/li[4]").click()
    assert driver.find_element(By.XPATH, "//h2[contains(text(),'Tablets')]").text == "Tablets"


def test_login_admin(driver, base_url):
    driver.get(base_url)
    driver.find_element(By.XPATH, "//body/nav[@id='top']/div[1]/div[2]/ul[1]/li[2]/div[1]/a[1]").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys("test_user")
    driver.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys("user_test")
    driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys("test1@mail.ru")
    driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys("test1")
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]").click()

def test_money(driver, base_url):
    driver.get(base_url)
    old_money = driver.find_element(By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[1]/form[1]/div[1]/a[1]").text
    driver.find_element(By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[1]/form[1]/div[1]/a[1]").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "€ Euro").click()
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[1]/form[1]/div[1]/a[1]").text != old_money


def test_value(driver, base_url):
    driver.get(base_url)
    old_value = driver.find_element(By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").text
    driver.find_element(By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[1]/form[1]/div[1]/a[1]").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "€ Euro").click()
    time.sleep(2)
    assert driver.find_element(By.XPATH,"//body/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]").text != old_value


def test_add_to_cart(driver, base_url):
    driver.get(base_url)
    driver.find_element(By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/button[1]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[3]/div[1]/button[1]").click()
    driver.find_element(By.LINK_TEXT, "View Cart").click()
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/table[1]/tfoot[1]/tr[1]/td[2]").text != ""

def test_admin(driver, base_url):
    driver.get(base_url + "/administration/")
    driver.find_element(By.CSS_SELECTOR, "#input-username").send_keys("user")
    driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys("bitnami")
    driver.find_element(By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/button[1]").click()
    driver.find_element(value="content")
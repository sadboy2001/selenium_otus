from selenium.webdriver.common.by import By


def test_search_input(driver, base_url):
    driver.get(base_url)
    driver.find_element(By.NAME, "search").send_keys("test")
    driver.find_element(By.CSS_SELECTOR, "#search button").click()
    driver.find_element(value="content")
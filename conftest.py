import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", choices=["chrome", "firefox"]
    )
    parser.addoption(
        "--headless", action='store_true'
    )
    parser.addoption(
        "--base_url", default='http:/localhost'
    )

# @pytest.fixture()
# def base_url(request):
#     return request.config.getoption("--base_url")

@pytest.fixture()
def driver(request):
    base_url = request.config.getoption("--base_url")
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    service = Service()

    if browser_name == "chrome":
        options = Options()
        if headless:
            options.add_argument("headless=new")
        browser = webdriver.Chrome(service=service, options=options)
        options = Options()
        options.headless = headless
    elif browser_name == "firefox":
        options = FirefoxOptions()
        browser = webdriver.Firefox(service=service, options=options)
        options.headless = headless
    else:
        raise NotImplemented()

    browser.maximize_window()
    browser.get(base_url)

    yield browser

    browser.close()
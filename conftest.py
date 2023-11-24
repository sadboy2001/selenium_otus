import time
import datetime

import pytest
import logging
import allure
import json

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
    parser.addoption(
        "--log_level", action="store", default="INFO"
    )


# @pytest.fixture()
# def base_url(request):
#     return request.config.getoption("--base_url")

@pytest.fixture()
def driver(request):
    base_url = request.config.getoption("--base_url")
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

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

    allure.attach(
        name=browser.session_id,
        body=json.dumps(browser.capabilities),
        attachment_type=allure.attachment_type.JSON)

    browser.log_level = log_level
    browser.logger = logger
    browser.test_name = request.node.name

    logger.info("Browser %s started" % browser)
    browser.maximize_window()
    browser.get(base_url)

    def fin():
        browser.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return browser

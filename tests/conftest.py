from time import sleep
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

pytest_plugins = [
    "fixtures.elements_collector",
    "fixtures.scripts_collector"
]


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('window-size=1920,1080')
    my_driver = webdriver.Chrome(options=options)
    my_driver.implicitly_wait(10)
    yield my_driver
    my_driver.quit()

from time import sleep

import requests
import json

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from .pages.home_page import HomePage
from .pages.profile_page import ProfilePage
from .pages.locators import profile_page_locators


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('window-size=1920,1080')
    my_driver = webdriver.Chrome(options=options)
    my_driver.implicitly_wait(10)
    yield my_driver
    my_driver.quit()


@pytest.fixture(scope='function')
def change_pass_back():
    yield
    session = requests.Session()
    data = {
        "login": "79964410394",
        "password": "R911t689012345",
        "remember": False
    }
    url = "https://apteka.magnit.ru/api/personal/auth/"

    session.post(url, data=data)

    url = "https://apteka.magnit.ru/api/personal/password/change/"

    data = {
        'password': 'R911t68901234%',
        'passwordConfirm': 'R911t68901234%',
        'currentPassword': 'R911t689012345'}

    session.post(url, data=data)

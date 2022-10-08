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


# @pytest.fixture(scope='function')
# def change_pass_back(driver):
#     yield
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_setting()
#     with allure.step("Изменить пароль пользователя обратно"):
#         with allure.step("Заполнить поле старый пароль"):
#             profile_page.find_element(profile_page_locators.old_pass).send_keys("R911t689012345")
#         with allure.step("Заполнить поле новый пароль"):
#             profile_page.find_element(profile_page_locators.new_pass).send_keys("R911t68901234%")
#         with allure.step("Заполнить поле новый пароль еще раз"):
#             profile_page.find_element(profile_page_locators.new_pass_again).send_keys("R911t68901234%")
#             sleep(5)
#         with allure.step("Нажать кнопку 'Создать новый пароль'"):
#             profile_page.find_element(profile_page_locators.new_pass_submit).click()
#             sleep(5)
#         with allure.step("Нажать кнопку Хорошо в открывшемся меню"):
#             profile_page.find_element(profile_page_locators.change_pass_ok_button).click()
#             sleep(5)


@pytest.fixture(scope='function')
def change_pass_back():
    yield
    url = "https://apteka.magnit.ru/api/personal/auth/"

    payload = json.dumps({
        "login": "79964410394",
        "password": "R911t689012345",
        "remember": False
    })
    headers = {
        'Content-Type': 'application/json'
    }

    requests.request("POST", url, headers=headers, data=payload)

    url = "https://apteka.magnit.ru/api/personal/password/change/"

    payload = {'password': 'R911t68901234%',
               'passwordConfirm': 'R911t68901234%',
               'currentPassword': 'R911t689012345'}
    files = [

    ]
    requests.request("POST", url, data=payload, files=files)
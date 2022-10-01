from time import sleep

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from ..pages.locators import base_page_locators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_elements(by_name, by_val)

    def go_to_main_page(self):
        self.find_element(base_page_locators.header_logo).click()
        sleep(5)

    def get_current_url(self):
        return self.driver.current_url

    def check_for_url_is_changed(self, current_url, url_that_should_be):
        with allure.step(f"Проверяем, что текущий url равен {url_that_should_be}"):
            assert current_url == url_that_should_be

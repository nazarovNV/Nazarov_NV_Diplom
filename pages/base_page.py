from time import sleep

import allure
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..pages.locators import home_page_locators
from ..pages.locators import base_page_locators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def is_element_visible(self, *args):
        by_name, by_val = args[0]
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by_name, by_val))
        )
        return self.driver.find_element(by_name, by_val)

    def is_not_element_present(self, *args):
        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def is_element_enable(self, *args):
        by_name, by_val = args[0]
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_value((by_name, by_val), "Войти")
        )
        # return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_elements(by_name, by_val)

    def go_to_main_page(self):
        self.find_element(base_page_locators.header_logo).click()
        sleep(2)

    def get_current_url(self):
        return self.driver.current_url

    def check_for_url_is_changed(self, current_url, url_that_should_be):
        with allure.step(f"Проверяем, что текущий url равен {url_that_should_be}"):
            assert current_url == url_that_should_be



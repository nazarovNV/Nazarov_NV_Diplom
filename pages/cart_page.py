import allure
from selenium.common import NoSuchElementException

from pages.base_page import BasePage

from pages.locators import cart_page_locators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_item_in_cart(self):
        with allure.step("Получить название товара в корзине"):
            return self.find_element(cart_page_locators.item_in_cart).text

    def check_item_is_in_cart(self, item_that_was_added, item_that_is_in_cart):
        with allure.step("Проверить что товар который был ранее добавлен находится в корзине"):
            assert item_that_was_added in item_that_is_in_cart, \
                "В корзине не тот товар который вы ранее добавили"

    def delete_item_from_cart(self):
        with allure.step("Удалить товар из корзины"):
            self.find_element(cart_page_locators.delete_item_button).click()

    def should_be_empty_cart(self):
        with allure.step("Проверить что корзина теперь пустая"):
            try:
                assert "Ваша корзина пока пуста" in \
                       self.find_element(cart_page_locators.your_cart_is_empty).text
            except NoSuchElementException:
                return False
            except AssertionError:
                return False
            return True

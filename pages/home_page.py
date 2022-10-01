from time import sleep

from selenium.common import NoSuchElementException

from ..pages.locators import base_page_locators
from ..pages.base_page import BasePage
from ..pages.locators import home_page_locators
import allure


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://apteka.magnit.ru/')

    def confirm_address(self):
        with allure.step("Подтвердить предложенный адрес"):
            self.find_element(home_page_locators.confirm_address_button).click()

    def go_to_login_screen(self):
        with allure.step("Нажать кнопку войти на главном экране"):
            self.find_element(home_page_locators.go_to_login_screen_button).click()

    def fill_login_inputs_valid_data_and_submit(self):
        with allure.step("Заполнить поле логин"):
            self.find_element(home_page_locators.login_input).send_keys("+79964410394")
        with allure.step("Заполнить поле пароль"):
            self.find_element(home_page_locators.password_input).send_keys("R911t68901234%")
        with allure.step("Нажать кнопку войти"):
            self.find_element(home_page_locators.submit_button).click()

    def fill_login_inputs_wrong_data_and_submit(self):
        with allure.step("Заполнить поле логин"):
            self.find_element(home_page_locators.login_input).send_keys("+79964410394")
        with allure.step("Заполнить поле пароль неверными данными"):
            self.find_element(home_page_locators.password_input).send_keys("R911t68901234%55")
        with allure.step("Нажать кнопку войти"):
            self.find_element(home_page_locators.submit_button).click()

    def add_item_to_cart(self):
        with allure.step("Добавить товар в корзину"):
            self.find_element(home_page_locators.buy_button).click()
            sleep(5)

    def get_item_that_i_added(self):
        with allure.step("Получить название товара который будет добавлен в корзину"):
            return self.find_element(home_page_locators.item_name).text

    def go_to_cart(self):
        with allure.step("Перейти в корзину пользователя"):
            self.find_element(home_page_locators.my_cart_button).click()
            sleep(2)

    def check_for_error_message(self):
        with allure.step("Проверить есть ли сообщение о неверном пароле"):
            try:
                self.find_element(home_page_locators.wrong_password_error)
            except NoSuchElementException:
                return False
            return True

    def go_to_profile_page(self):
        with allure.step("Перейти в профиль пользователя"):
            self.find_element(home_page_locators.user_logo).click()

    def get_user_name(self):
        with allure.step("Получить имя пользователя"):
            return self.find_element(home_page_locators.user_logo_user_name).text

    def fill_login_inputs_with_new_pass_and_submit(self):
        with allure.step("Заполнить поле логин"):
            self.find_element(home_page_locators.login_input).send_keys("+79964410394")
        with allure.step("Заполнить поле пароль"):
            self.find_element(home_page_locators.password_input).send_keys("R911t689012345")
        with allure.step("Нажать кнопку войти"):
            self.find_element(home_page_locators.submit_button).click()

    def click_company_info_link(self):
        with allure.step("Нажать на ссылку 'Информация о компании'"):
            self.find_element(home_page_locators.company_info_link).click()

    def click_contacts_link(self):
        with allure.step("Нажать на ссылку 'Контакты'"):
            self.find_element(home_page_locators.contacts_link).click()

    def click_feedback_link(self):
        with allure.step("Нажать на ссылку 'Обратная связь'"):
            self.find_element(home_page_locators.feedback_link).click()

    def click_how_to_order_link(self):
        with allure.step("Нажать на ссылку 'Как сделать заказ'"):
            self.find_element(home_page_locators.how_to_order_link).click()

    def click_payment_link(self):
        with allure.step("Нажать на ссылку 'Оплата'"):
            self.find_element(home_page_locators.payment_link).click()

    def click_return_link(self):
        with allure.step("Нажать на ссылку 'Возврат товара'"):
            self.find_element(home_page_locators.return_link).click()

    def click_promo_rules_link(self):
        with allure.step("Нажать на ссылку 'Правила применения скидок'"):
            self.find_element(home_page_locators.promo_rules_link).click()

    def click_medication_release_link(self):
        with allure.step("Нажать на ссылку 'Порядок отпуска лекарственных средств'"):
            self.find_element(home_page_locators.medication_release_link).click()

    def click_politics_personal_data_link(self):
        with allure.step("Нажать на ссылку 'Политика обработки персональных данных'"):
            self.find_element(home_page_locators.politics_personal_data_link).click()

    def click_terms_of_use_link(self):
        with allure.step("Нажать на ссылку 'Пользовательское соглашение'"):
            self.find_element(home_page_locators.terms_of_use_link).click()

    def click_legal_information_link(self):
        with allure.step("Нажать на ссылку 'Правовая информация'"):
            self.find_element(home_page_locators.legal_information_link).click()

    def check_number_of_big_banners_eq_5(self):
        with allure.step("Проверить, что на странице есть 5 больших банеров"):
            assert len(self.find_elements(home_page_locators.big_banners)) == 5

    def check_if_second_banner_is_visible(self):
        with allure.step("Проверить, что картинка второго банера видна"):
            assert self.find_element(home_page_locators.second_banner_img).is_displayed()





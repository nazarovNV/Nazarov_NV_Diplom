import string
import random
import datetime
from time import sleep
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys

from ..pages.locators import home_page_locators
from ..pages.base_page import BasePage
from ..pages.locators import profile_page_locators
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_my_data(self):
        with allure.step("Перейти на вкладку личные данные"):
            sleep(3)
            self.is_element_visible(profile_page_locators.my_data_tab).click()
            sleep(3)

    def can_not_see_login_form(self):
        assert self.is_not_element_present(home_page_locators.login_window)

    def change_second_name(self):
        with allure.step("Изменить фамилию пользователя"):
            rand_string = ''.join(random.choice('абвгдежзийклмнопрстуфхцчшщъыьэюя') for i in range(8))
            self.find_element(profile_page_locators.my_second_name_input).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_second_name_input).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_second_name_input).send_keys(rand_string)
            return rand_string

    def check_for_my_orders_tab_on_page(self):
        with allure.step("Проверить залогинился ли пользователь"):
            try:
                self.find_element(profile_page_locators.my_orders_tab)
            except NoSuchElementException:
                return False
            return True

    def save_data(self):
        with allure.step("Нажать кнопку сохранить"):
            self.find_element(profile_page_locators.save_data).click()

    def change_name(self):
        with allure.step("Изменить имя пользователя"):
            rand_string = ''.join(random.choice('абвгдежзийклмнопрстуфхцчшщъыьэюя') for i in range(8))
            self.find_element(profile_page_locators.my_name_input).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_name_input).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_name_input).send_keys(rand_string)
            return rand_string

    def get_name(self):
        with allure.step("Получить имя пользователя"):
            return self.is_element_visible(profile_page_locators.my_name_input).get_attribute('value')

    def get_second_name(self):
        with allure.step("Получить фамилию пользователя"):
            return self.find_element(profile_page_locators.my_second_name_input).get_attribute('value')

    def exit_profile(self):
        with allure.step("Выйти из профиля пользователя"):
            self.find_element(profile_page_locators.exit_profile).click()
            # sleep(5)

    def change_patronymic(self):
        with allure.step("Изменить имя пользователя"):
            rand_string = ''.join(random.choice('абвгдежзийклмнопрстуфхцчшщъыьэюя') for i in range(8))
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(rand_string)
            return rand_string

    def get_patronymic(self):
        with allure.step("Получить фамилию пользователя"):
            return self.find_element(profile_page_locators.my_patronymic_input).get_attribute('value')

    def change_email(self):
        with allure.step("Изменить имя пользователя"):
            rand_string = ''.join(random.choice(string.ascii_letters) for i in range(30))
            self.find_element(profile_page_locators.my_email).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_email).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_email).send_keys(rand_string + "@gmail.com")
            return rand_string + "@gmail.com"

    def get_email(self):
        with allure.step("Получить фамилию пользователя"):
            return self.find_element(profile_page_locators.my_email).get_attribute('value')

    def change_date_of_birth(self):
        with allure.step("Изменить дату рождения пользователя"):
            fake = Faker()
            start_date = datetime.date(year=1911, month=1, day=1)
            end_date = datetime.date(year=2003, month=1, day=1)
            c = fake.date_between(start_date=start_date, end_date=end_date)
            date_object = datetime.datetime.strftime(c, '%d.%m.%Y')
            self.find_element(profile_page_locators.my_date_of_birth).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_date_of_birth).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_date_of_birth).send_keys(date_object)
            return date_object

    def get_date_of_birth(self):
        with allure.step("Получить дату рождения пользователя"):
            return self.find_element(profile_page_locators.my_date_of_birth).get_attribute('value')

    def change_gender(self):
        with allure.step("Изменить пол пользователя"):
            if self.find_element(profile_page_locators.my_gender).text == "Женский":
                self.find_element(profile_page_locators.my_gender).click()
                self.find_element(profile_page_locators.my_gender_man_option).click()
            else:
                self.find_element(profile_page_locators.my_gender).click()
                self.find_element(profile_page_locators.my_gender_women_option).click()

    def get_gender(self):
        with allure.step("Получить пол пользователя"):
            return self.find_element(profile_page_locators.my_gender).text

    def change_date_of_birth_minor_user(self):
        with allure.step("Изменить дату рождения пользователя на дату несовершеннолетнего пользователя"):
            self.find_element(profile_page_locators.my_date_of_birth).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_date_of_birth).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_date_of_birth).send_keys("13.03.2013")

    def check_for_error_date_of_birth_minor_user(self):
        with allure.step("Проверить, что сообщение 'Возраст должен быть совершеннолетним'"):
            sleep(3)
            assert self.find_element(profile_page_locators.error_date_of_birth).text == \
                   "Возраст должен быть совершеннолетним", \
                "Ошибка 'Возраст должен быть совершеннолетним' не отображается"

    def change_date_of_birth_incorrect_data(self):
        with allure.step("Изменить дату рождения пользователя на некорректную"):
            self.find_element(profile_page_locators.my_date_of_birth).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_date_of_birth).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_date_of_birth).send_keys("50.50.2000")

    def check_for_error_date_of_birth_incorrect_data(self):
        with allure.step("Проверить, что сообщение 'Месяц введен некорректный'"):
            sleep(3)
            assert self.find_element(profile_page_locators.error_date_of_birth).text == \
                   "Месяц введен некорректный", \
                "Ошибка 'Месяц введен некорректный' не отображается"

    def go_to_my_setting(self):
        with allure.step("Перейти на вкладку настройки"):
            sleep(5)
            self.find_element(profile_page_locators.my_setting_tab).click()
            sleep(5)

    def change_password_in_profile(self):
        with allure.step("Изменить пароль пользователя"):
            with allure.step("Заполнить поле старый пароль"):
                self.find_element(profile_page_locators.old_pass).send_keys("R911t68901234%")
            with allure.step("Заполнить поле новый пароль"):
                self.find_element(profile_page_locators.new_pass).send_keys("R911t689012345")
            with allure.step("Заполнить поле новый пароль еще раз"):
                self.find_element(profile_page_locators.new_pass_again).send_keys("R911t689012345")
                sleep(1)
            with allure.step("Нажать кнопку сохранить"):
                self.find_element(profile_page_locators.new_pass_submit).click()
                sleep(5)
            with allure.step("Нажать кнопку Хорошо в открывшемся меню"):
                self.find_element(profile_page_locators.change_pass_ok_button).click()
                sleep(5)

    def should_be_open_personal_page(self):
        assert self.is_element_visible(profile_page_locators.profile_menu), \
            "Страница личного кабинета пользователя не открылась"

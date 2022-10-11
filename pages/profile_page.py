import string
import random
import datetime
from time import sleep
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys

from pages.locators import home_page_locators
from pages.base_page import BasePage
from pages.locators import profile_page_locators
from faker import Faker


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_my_data(self):
        with allure.step("Перейти на вкладку личные данные"):
            self.is_element_visible(profile_page_locators.my_data_tab).click()

    def go_to_my_orders(self):
        with allure.step("Перейти на вкладку 'Мои заказы'"):
            self.is_element_visible(profile_page_locators.my_orders_tab).click()

    def go_to_my_favorites(self):
        with allure.step("Перейти на вкладку 'Избранное'"):
            self.is_element_visible(profile_page_locators.my_favorites_tab).click()

    def get_item_in_favorites(self):
        with allure.step("Получить название товара в избранном"):
            return self.find_element(profile_page_locators.item_in_favorites).text

    def change_second_name(self):
        with allure.step("Изменить фамилию пользователя"):
            rand_string = ''.join(random.choice('абвгдежзийклмнопрстуфхцчшщъыьэюя') for i in range(8))
            self.find_element(profile_page_locators.my_second_name_input).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_second_name_input).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_second_name_input).send_keys(rand_string)
            return rand_string

    def change_second_name_with_wrong_data(self):
        with allure.step("Заполнить поле 'Фамилия' не валидными данными"):
            rand_string = ''.join(random.choice('1234567890') for i in range(8))
            self.find_element(profile_page_locators.my_second_name_input).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_second_name_input).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_second_name_input).send_keys(rand_string)
            return rand_string

    def change_second_name_with_empty_data(self):
        with allure.step("Заполнить фамилия пользователя пустой строкой"):
            empty_string = ''
            self.find_element(profile_page_locators.my_second_name_input).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_second_name_input).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_second_name_input).send_keys("")
            return empty_string

    def change_patronymic_with_wrong_data(self):
        with allure.step("Заполнить отчество пользователя неверными данными"):
            rand_string = ''.join(random.choice('1234567890') for i in range(8))
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(rand_string)
            return rand_string

    def change_patronymic_with_empty_data(self):
        with allure.step("Заполнить отчество пользователя пустой строкой"):
            empty_string = ''
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(Keys.DELETE)
            return empty_string

    def check_for_my_orders_tab_on_page(self):
        with allure.step("Проверить залогинился ли пользователь"):
            try:
                self.find_element(profile_page_locators.my_orders_tab)
            except NoSuchElementException:
                return False
            return True

    def remove_item_from_favorites(self):
        with allure.step("Убрать товар из избранного"):
            self.find_element(home_page_locators.add_to_favorite_btn).click()

    def check_is_user_auth(self):
        with allure.step("Проверить залогинился ли пользователь"):
            try:
                self.is_element_visible(profile_page_locators.my_orders_tab)
            except NoSuchElementException:
                return False
            return True

    def save_data(self):
        with allure.step("Нажать кнопку сохранить"):
            self.find_element(profile_page_locators.save_data).click()
            sleep(2)

    def change_name(self):
        with allure.step("Изменить имя пользователя"):
            rand_string = ''.join(random.choice('абвгдежзийклмнопрстуфхцчшщъыьэюя') for i in range(8))
            self.find_element(profile_page_locators.my_name_input).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_name_input).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_name_input).send_keys(rand_string)
            return rand_string

    def change_name_with_number(self):
        with allure.step("Изменить имя пользователя цифрами"):
            rand_string = ''.join(random.choice('1234567890') for i in range(8))
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
            self.is_not_element_present(profile_page_locators.exit_profile)

    def change_patronymic(self):
        with allure.step("Изменить имя пользователя"):
            rand_string = ''.join(random.choice('абвгдежзийклмнопрстуфхцчшщъыьэюя') for i in range(8))
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_patronymic_input).send_keys(rand_string)
            return rand_string

    def get_patronymic(self):
        with allure.step("Получить отчество пользователя"):
            return self.find_element(profile_page_locators.my_patronymic_input).get_attribute('value')

    def change_email(self):
        with allure.step("Изменить почту пользователя"):
            rand_string = ''.join(random.choice(string.ascii_letters) for i in range(30))
            self.find_element(profile_page_locators.my_email).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_email).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_email).send_keys(rand_string + "@gmail.com")
            return rand_string + "@gmail.com"

    def change_email_wrong_data(self):
        with allure.step("Изменить имя пользователя"):
            rand_string = ''.join(random.choice(string.ascii_letters) for i in range(30))
            self.find_element(profile_page_locators.my_email).send_keys(Keys.CONTROL + "a")
            self.find_element(profile_page_locators.my_email).send_keys(Keys.DELETE)
            self.find_element(profile_page_locators.my_email).send_keys(rand_string)
            return rand_string

    def get_email(self):
        with allure.step("Получить Дату рождения пользователя"):
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
            assert self.find_element(profile_page_locators.error_date_of_birth).text == \
                   "Месяц введен некорректный", \
                   "Ошибка 'Месяц введен некорректный' не отображается"

    def check_for_error_name_with_number_incorrect_data(self):
        with allure.step("Проверить, что сообщение 'Разрешены только буквы, дефисы и пробелы' отображается"):
            assert self.find_element(profile_page_locators.error_date_of_birth).text == \
                   "Разрешены только буквы, дефисы и пробелы", \
                   "Ошибка 'Разрешены только буквы, дефисы и пробелы' не отображается"

    def check_for_error_email_wrong_data(self):
        with allure.step("Проверить, что сообщение "
                         "'Адрес электронной почты должен содержать символ @, разрешены символы . - и _'"):
            assert self.find_element(profile_page_locators.error_email_wrong_data).text == \
                   "Адрес электронной почты должен содержать символ @, разрешены символы . - и _", \
                   "Ошибка 'Адрес электронной почты должен содержать символ @, разрешены символы . - и _' " \
                   "не отображается"

    def go_to_my_setting(self):
        with allure.step("Перейти на вкладку настройки"):
            self.find_element(profile_page_locators.my_setting_tab).click()

    def change_password_in_profile(self):
        with allure.step("Изменить пароль пользователя"):
            with allure.step("Заполнить поле старый пароль"):
                self.find_element(profile_page_locators.old_pass).send_keys("R911t68901234%")
            with allure.step("Заполнить поле новый пароль"):
                self.find_element(profile_page_locators.new_pass).send_keys("R911t689012345")
            with allure.step("Заполнить поле новый пароль еще раз"):
                self.find_element(profile_page_locators.new_pass_again).send_keys("R911t689012345")
            with allure.step("Проверяем, что данные заполнены и можно нажимать кнопку 'Создать новый пароль'"):
                assert self.is_element_visible(profile_page_locators.change_pass_filled)
            with allure.step("Нажать кнопку 'Создать новый пароль'"):
                sleep(2)
                self.find_element(profile_page_locators.new_pass_submit).click()
            with allure.step("Нажать кнопку Хорошо в открывшемся меню"):
                assert self.is_element_visible(profile_page_locators.change_pass_ok_button)
                self.find_element(profile_page_locators.change_pass_ok_button).click()

    def check_item_is_in_favorites(self, item_that_was_added, item_that_is_in_favorites):
        with allure.step("Проверить что товар который был ранее добавлен в избранном находится в избранном"):
            assert item_that_was_added in item_that_is_in_favorites, \
                "В избранном не тот товар который вы ранее добавили"

    def should_be_empty_in_favorites(self):
        with allure.step("Проверить что нет товаров в избранном"):
            try:
                assert "Ваш список пока пуст" in \
                       self.find_element(profile_page_locators.no_items_in_favorites).text
            except NoSuchElementException:
                return False
            except AssertionError:
                return False
            return True

    def should_be_empty_in_orders(self):
        with allure.step("Проверить что во вкладке 'Заказы' нет заказов"):
            try:
                assert "У Вас пока нет заказов" in \
                       self.find_element(profile_page_locators.you_do_not_have_orders_yet).text
            except NoSuchElementException:
                return False
            except AssertionError:
                return False
            return True

    def should_be_orders_in_orders(self):
        with allure.step("Проверить что во вкладке 'Заказы' есть заказы"):
            try:
                assert "Заказ №: 9017421" in \
                       self.find_element(profile_page_locators.order_item_id).text
            except NoSuchElementException:
                return False
            except AssertionError:
                return False
            return True

    def go_to_done_orders_tab(self):
        with allure.step("Перейти на вкладку 'Выполненные'"):
            self.is_element_visible(profile_page_locators.done_orders_tab).click()

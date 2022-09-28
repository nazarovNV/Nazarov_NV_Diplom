from time import sleep

import allure
from allure import title, step
from pytest import fixture


# <-------------------------------=1-1=------------------------------->
@title("Переход на главную страницу")
@fixture()
def select_address_0(go_to_main_page, element, driver):
    with step("Переход на главную страницу степ"):
        go_to_main_page


# <-------------------------------=1-2=------------------------------->
@title("Нажатие кнопки 'Выбрать адрес'")
@fixture()
def select_address_1(select_address_0, element_chose_address, element, driver):
    select_address_0
    element_chose_address.click()


# <-------------------------------=1-3=------------------------------->
@title("Заполнение поля адреса")
@fixture()
def select_address_2(select_address_1, element_chose_address_input_field, element, driver):
    select_address_1
    element_chose_address_input_field.send_keys('Солнечная улица, 15/5')


# <-------------------------------=1-3=------------------------------->
@title("Выбрать адрес из предложенного списка")
@fixture()
def select_address_3(select_address_2, element_chose_address_drop_down_list, element, driver):
    select_address_2
    element_chose_address_drop_down_list.click()
    sleep(5)


# <-------------------------------=1-4=------------------------------->
@title("Нажатие кнопки 'Выбрать'")
@fixture()
def select_address_4(select_address_3, element_chose_address_input_field_submit, element, driver):
    select_address_3
    element_chose_address_input_field_submit.click()
    sleep(5)


# <-------------------------------=1-5=------------------------------->
@title("Проверка того, что введенный адрес соответствует отображаемому")
@fixture()
def select_address_5(select_address_4, element_user_address, element, driver):
    select_address_4
    assert element_user_address.text == 'Солнечная улица, 15/5'


from time import sleep

import allure
import pytest


# <-------------------------------=1-1=------------------------------->

@pytest.fixture()
def select_address_0(go_to_main_page, element, driver):
    go_to_main_page


@pytest.fixture()
def select_address_1(select_address_0, element_chose_address, element, driver):
    select_address_0
    element_chose_address.click()
    print("select_address_1 done")

@pytest.fixture()
def select_address_2(select_address_1, element_chose_address_input_field, element, driver):
    select_address_1
    element_chose_address_input_field.send_keys('Солнечная улица 15/5')
    print("select_address_2 done")
    sleep(5)

@pytest.fixture()
def select_address_3(select_address_2, element_chose_address_drop_down_list, element, driver):
    select_address_2
    element_chose_address_drop_down_list.click()
    print("select_address_3 done")

@pytest.fixture()
def select_address_4(select_address_3, element_chose_address_input_field_submit, element, driver):
    select_address_3
    element_chose_address_input_field_submit.click()
    print("select_address_4 done")
    sleep(10)



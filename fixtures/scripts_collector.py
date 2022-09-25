import allure
import pytest


# <-------------------------------=1-1=------------------------------->

@pytest.fixture()
def select_address_0(go_to_main_page, element, driver):
    go_to_main_page()


@pytest.fixture()
def select_address_1(select_address_0, element_chose_address, element, driver):
    select_address_0
    element_chose_address.click()

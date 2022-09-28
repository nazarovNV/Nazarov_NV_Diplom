import pytest
from selenium.webdriver.common.by import By


# Поиск элемента

@pytest.fixture()
def element(driver):
    return driver.find_element


@pytest.fixture()
def url(driver):
    return driver.get


# Локатор элемента
@pytest.fixture()
def element_chose_address(element):
    return element(By.CLASS_NAME, "select-address-header")


@pytest.fixture()
def element_chose_address_input_field(element):
    return element(By.CSS_SELECTOR, ".m-modal-delivery-address .m-input-text__input")


@pytest.fixture()
def element_chose_address_drop_down_list(element):
    return element(By.CLASS_NAME, "m-input-address__suggestions__item--name")


@pytest.fixture()
def element_chose_address_input_field_submit(element):
    return element(By.CLASS_NAME, "user-address-map__form-submit")


@pytest.fixture()
def go_to_main_page(url):
    return url("https://dostavka.magnit.ru/")


@pytest.fixture()
def element_search_input(element):
    return element(By.CLASS_NAME, "m-input-text__input")


@pytest.fixture()
def element_user_address(element):
    return element(By.CLASS_NAME, "select-address-header--text")

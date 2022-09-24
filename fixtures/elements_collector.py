import pytest
from selenium.webdriver.common.by import By

# Поиск элемента

@pytest.fixture()
def element(driver):
    return driver.find_element


# Локатор элемента
@pytest.fixture()
def element_chose_address(element):
    return element(By.CLASS_NAME, "select-address-header")

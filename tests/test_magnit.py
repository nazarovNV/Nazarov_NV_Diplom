import allure


# <-------------------------------=1=------------------------------->
@allure.feature("Главная страница")
@allure.story("Выбор адреса доставки")
def test_select_address(select_address_0):
    select_address_0

import allure


# <-------------------------------=1=------------------------------->
@allure.feature("Главная страница")
@allure.story("Выбор адреса доставки")
def test_select_address(select_address_4):
    select_address_4

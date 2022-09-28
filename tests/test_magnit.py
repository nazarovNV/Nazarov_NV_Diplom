from allure import step, title, description, suite


# <-------------------------------=1=------------------------------->
# @allure.feature("Главная страница")
# @allure.story("Выбор адреса доставки")
@title("Выбор адреса при первом посещении приложения")
@suite("Выбор адреса")
def test_select_address(select_address_5):
    select_address_5

# <-------------------------------=2=------------------------------->

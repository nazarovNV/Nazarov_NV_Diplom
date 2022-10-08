from time import sleep
from ..pages.cart_page import CartPage
from ..pages.home_page import HomePage
from ..pages.profile_page import ProfilePage
import allure


# @allure.suite("Авторизация")
# @allure.title("Авторизация с валидными данными")
# def test_login(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     assert profile_page.check_for_my_orders_tab_on_page(), "Вы не авторизовались"
#

# @allure.suite("Авторизация")
# @allure.title("Авторизация с невалидными данными")
# def test_login_wrong_password(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_wrong_data_and_submit()
#     assert home_page.check_for_error_message(), "Нет сообщения о неверном пароле"


# @allure.suite("Изменение данных пользователя")
# @allure.title("Имя на иконке пользователя на главной странице меняется если изменить имя")
# def test_change_name_at_profile_icon(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)

#     profile_page.go_to_my_data()
#     new_name = profile_page.change_name()
#     profile_page.save_data()
#     profile_page.go_to_main_page()
#     home_page = HomePage(driver)
#     home_page.is_name_changed(new_name)
#     assert home_page.get_user_name() == new_name, "Имя не изменилось"


# @allure.suite("Изменение данных пользователя")
# @allure.title("Изменение имени пользователя и проверка имени после повторной авторизации")
# def test_change_name(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#
#     profile_page.go_to_my_data()
#     new_name = profile_page.change_name()
#     profile_page.save_data()
#
#     profile_page.exit_profile()
#     home_page = HomePage(driver)
#     home_page.is_it_homepage()
#     home_page.is_client_logged_out()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#     assert profile_page.get_name() == new_name, "Имя не изменилось"


# @allure.suite("Изменение данных пользователя")
# @allure.title("Изменение фамилии пользователя и проверка фамилии после повторной авторизации")
# def test_change_second_name(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     new_second_name = profile_page.change_second_name()
#     profile_page.save_data()
#
#     profile_page.exit_profile()
#
#     home_page = HomePage(driver)
#
#     home_page.is_it_homepage()
#     home_page.is_client_logged_out()
#
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     assert profile_page.get_second_name() == new_second_name, "Фамилия не изменилась"

# @allure.suite("Изменение данных пользователя")
# @allure.title("Изменение отчества пользователя и проверка отчества после повторной авторизации")
# def test_change_patronymic(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     new_patronymic = profile_page.change_patronymic()
#     profile_page.save_data()
#
#     profile_page.exit_profile()
#
#     home_page = HomePage(driver)
#
#     home_page.is_it_homepage()
#     home_page.is_client_logged_out()
#
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     assert profile_page.get_patronymic() == new_patronymic, "Отчество не изменилось"
#
#
# @allure.suite("Изменение данных пользователя")
# @allure.title("Изменение почты пользователя и проверка почты после повторной авторизации")
# def test_change_email(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     new_email = profile_page.change_email()
#     profile_page.save_data()
#
#     profile_page.exit_profile()
#
#     home_page = HomePage(driver)
#
#     home_page.is_it_homepage()
#     home_page.is_client_logged_out()
#
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     assert profile_page.get_email() == new_email, "Почта не изменилась"


# @allure.suite("Изменение данных пользователя")
# @allure.title("Изменение даты рождения пользователя и проверка даты рождения после повторной авторизации")
# def test_change_date_of_birth(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     new_date_of_birth = profile_page.change_date_of_birth()
#     profile_page.save_data()
#
#     profile_page.exit_profile()
#
#     home_page = HomePage(driver)
#
#     home_page.is_it_homepage()
#     home_page.is_client_logged_out()
#
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     assert profile_page.get_date_of_birth() == new_date_of_birth, "Дата рождения не изменилась"


# @allure.suite("Изменение данных пользователя")
# @allure.title("Изменение пола пользователя и проверка пола после повторной авторизации")
# def test_change_gender(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     old_gender = profile_page.get_gender()
#     profile_page.change_gender()
#
#     profile_page.save_data()
#     profile_page.exit_profile()
#
#     home_page = HomePage(driver)
#
#     home_page.is_it_homepage()
#     home_page.is_client_logged_out()
#
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     assert profile_page.get_gender() != old_gender, "Пол не изменился"
#
#
# @allure.suite("Изменение данных пользователя")
# @allure.title("Проверка того, что нельзя поставить дату несовершеннолетнего пользователя")
# def test_error_date_of_birth_minor_user(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     profile_page.change_date_of_birth_minor_user()
#     profile_page.check_for_error_date_of_birth_minor_user()
#
#
# @allure.suite("Изменение данных пользователя")
# @allure.title("Проверка того, что нельзя поставить некорректную дату")
# def test_date_of_birth_incorrect_data(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     profile_page.go_to_my_data()
#
#     profile_page.change_date_of_birth_incorrect_data()
#
#     profile_page.check_for_error_date_of_birth_incorrect_data()
#
#
@allure.suite("Изменение данных пользователя")
@allure.title("Проверка возможности авторизоваться после смены пароля")
def test_change_password(driver, change_pass_back):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()
    home_page.go_to_login_screen()
    home_page.can_see_login_form()
    home_page.fill_login_inputs_valid_data_and_submit()
    profile_page = ProfilePage(driver)

    profile_page.go_to_my_setting()
    profile_page.change_password_in_profile()

    profile_page.exit_profile()

    home_page = HomePage(driver)

    home_page.is_it_homepage()
    home_page.is_client_logged_out()

    home_page.go_to_login_screen()
    home_page.fill_login_inputs_with_new_pass_and_submit()
    profile_page = ProfilePage(driver)
    assert profile_page.check_for_my_orders_tab_on_page(), "Вы не авторизовались"


# @allure.suite("Корзина")
# @allure.title("Добавление товара в корзину(не авторизованный пользователь)")
# def test_add_item(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     item_that_was_added = home_page.get_item_that_i_added()
#     home_page.add_item_to_cart()
#     home_page.can_see_number_in_cart()
#     home_page.go_to_cart()
#     cart_page = CartPage(driver)
#     item_that_is_in_cart = cart_page.get_item_in_cart()
#     cart_page.check_item_is_in_cart(item_that_was_added, item_that_is_in_cart)

# @allure.suite("Корзина")
# @allure.title("Удаление товара из корзины(не авторизованный пользователь)")
# def test_delete_item_from_cart_no_auth(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.add_item_to_cart()
#     home_page.can_see_number_in_cart()
#     home_page.go_to_cart()
#     cart_page = CartPage(driver)
#     cart_page.delete_item_from_cart()
#     cart_page.should_be_empty_cart()

# @allure.suite("Корзина")
# @allure.title("Удаление товара из корзины(авторизованный пользователь)")
# def test_delete_item_from_cart_auth(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.go_to_login_screen()
#     home_page.can_see_login_form()
#     home_page.fill_login_inputs_valid_data_and_submit()
#     profile_page = ProfilePage(driver)
#     sleep(5)
#     profile_page.go_to_main_page()
#     home_page.is_it_homepage()
#
#     home_page.add_item_to_cart()
#     home_page.can_see_number_in_cart()
#     home_page.go_to_cart()
#     cart_page = CartPage(driver)
#     cart_page.delete_item_from_cart()
#     cart_page.should_be_empty_cart()
##################

#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Информация о компании'")
# def test_link_company_info(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_company_info_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/about-magnit/")
#
#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Контакты'")
# def test_link_contacts(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_contacts_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/contacts/")
#
#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Обратная связь'")
# def test_link_feedback(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_feedback_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/feedback/")
#
#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Как сделать заказ'")
# def test_link_how_to_order(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_how_to_order_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/how_to_order")
#
#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Как сделать заказ'")
# def test_link_payment(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_payment_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/payment")
#
#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Возврат товара'")
# def test_link_return(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_return_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/return")
#
#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Правила применения скидок'")
# def test_link_promo_rules(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_promo_rules_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/promo-rules")
#
#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Порядок отпуска лекарственных средств'")
# def test_link_medication_release(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_medication_release_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/medication_release")
#
#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Политика обработки персональных данных'")
# def test_link_politics_personal_data(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_politics_personal_data_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/politics_personal_data")
#
#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Пользовательское соглашение'")
# def test_link_terms_of_use(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_terms_of_use_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/terms_of_use/")
#
#
# @allure.suite("Работа ссылок")
# @allure.title("Проверка работы ссылки 'Правовая информация'")
# def test_link_legal_information(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#
#     home_page.click_legal_information_link()
#     home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/legal_information/")
#
#
# @allure.suite("Баннеры акций")
# @allure.title("Проверка наличия 5 баннеров")
# def test_should_be_5_banners(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.check_number_of_big_banners_eq_5()
#
#
# @allure.suite("Баннеры акций")
# @allure.title("Проверка работы карусели больших банеров и их отображения")
# def test_big_banners_carousel(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     home_page.confirm_address()
#     home_page.check_if_first_banner_is_visible()
#     home_page.click_next_big_banner()
#     home_page.check_if_second_banner_is_visible()
#     home_page.click_next_big_banner()
#     home_page.check_if_third_banner_is_visible()
#     home_page.click_next_big_banner()
#     home_page.check_if_fourth_banner_is_visible()
#     home_page.click_next_big_banner()
#     home_page.check_if_fifth_banner_is_visible()
#
#     home_page.click_previous_big_banner()
#     home_page.check_if_fourth_banner_is_visible()
#     home_page.click_previous_big_banner()
#     home_page.check_if_third_banner_is_visible()
#     home_page.click_previous_big_banner()
#     home_page.check_if_second_banner_is_visible()
#     home_page.click_previous_big_banner()
#     home_page.check_if_first_banner_is_visible()

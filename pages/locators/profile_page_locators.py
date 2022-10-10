from selenium.webdriver.common.by import By

my_data_tab = (By.CSS_SELECTOR, 'a[data-test-id="personal-data-tab"]')
my_setting_tab = (By.CSS_SELECTOR, 'a[data-test-id="option-tab"]')
my_orders_tab = (By.CSS_SELECTOR, 'a[data-test-id="my-order-tab"]')
my_favorites_tab = (By.CSS_SELECTOR, 'a[data-test-id="favorite-tab"]')

my_second_name_input = (By.CSS_SELECTOR, 'input[placeholder="Фамилия"]')
my_name_input = (By.CSS_SELECTOR, 'input[placeholder="Имя"]')
my_patronymic_input = (By.CSS_SELECTOR, 'input[placeholder="Отчество"]')
my_email = (By.CSS_SELECTOR, 'input[placeholder="Эл. почта"]')
my_date_of_birth = (By.CSS_SELECTOR, 'input[placeholder="дд.мм.гггг"]')
my_gender = (By.CSS_SELECTOR, '.b-field__caption')
my_gender_man_option = (By.CSS_SELECTOR, '.b-field__options :nth-child(1)')
my_gender_women_option = (By.CSS_SELECTOR, '.b-field__options :nth-child(2)')

old_pass = (By.CSS_SELECTOR, 'input[placeholder="Введите старый пароль"]')
new_pass = (By.CSS_SELECTOR, 'input[placeholder="Введите новый пароль"]')
new_pass_again = (By.CSS_SELECTOR, 'input[placeholder="Введите новый пароль ещё раз"]')
new_pass_submit = (By.CSS_SELECTOR, 'button[data-test-id="button-save"]')
change_pass_ok_button = (By.CSS_SELECTOR,
                         'div[data-test-id="popup-item"]  button[data-test-id="success-password-button"]')
change_pass_filled = (By.CSS_SELECTOR, '.b-profile-settings__row:nth-child(4) div.b-field.is-filled')

profile_menu = (By.XPATH, ".//*[@data-test-id='profile']")

error_date_of_birth = (By.CSS_SELECTOR, '.b-field__error')
error_name_with_numbers = (By.CSS_SELECTOR, '.b-field__error')
error_email_wrong_data = (By.CSS_SELECTOR, '.b-field__error')


save_data = (By.CSS_SELECTOR, 'button[data-test-id="button-save"]')
exit_profile = (By.CSS_SELECTOR, '.b-profile__menu-item[data-test-id="exit"]')

item_in_favorites = (By.CSS_SELECTOR, '.product-card__title')
no_items_in_favorites = (By.CSS_SELECTOR, '.b-profile-favorites__title')

you_do_not_have_orders_yet = (By.CSS_SELECTOR, '.b-profile-orders__wrapper div div')
done_orders_tab = (By.CSS_SELECTOR, 'div[data-test-id="done-orders-tab"]')
order_item_id = (By.CSS_SELECTOR, '.b-profile-order__title--active')






from selenium.webdriver.common.by import By


my_data_tab = (By.CSS_SELECTOR, 'a[data-test-id="personal-data-tab"]')
my_setting_tab = (By.CSS_SELECTOR, 'a[data-test-id="option-tab"]')
my_orders_tab = (By.CSS_SELECTOR, 'a[data-test-id="my-order-tab"]')

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




error_date_of_birth = (By.CSS_SELECTOR, '.b-field__error')

save_data = (By.CSS_SELECTOR, 'button[data-test-id="button-save"]')
exit_profile = (By.CSS_SELECTOR, '.b-profile__menu-item[data-test-id="exit"]')


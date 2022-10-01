from selenium.webdriver.common.by import By


sign_in_button = (By.CLASS_NAME, 'login')
go_to_login_screen_button = (By.CSS_SELECTOR,
                             'div[class="header__userzone-image header__userzone-image--auth"]')
confirm_address_button = (By.CSS_SELECTOR, '.b-location-confirmation__buttons-list button')
login_input = (By.CSS_SELECTOR, 'input[placeholder="Телефон или электронная почта"]')
password_input = (By.CSS_SELECTOR, 'input[placeholder="Пароль"]')
submit_button = (By.CSS_SELECTOR, 'button[data-test-id="button-login"]')
buy_button = (By.CSS_SELECTOR, 'button[data-test-id="product-buy-btn"]')
item_name = (By.CSS_SELECTOR, '.product-card__title')
my_cart_button = (By.CSS_SELECTOR, '.header__userzone-control--basket')
wrong_password_error = (By.CSS_SELECTOR, '.upblock__content .error')
user_logo = (By.CSS_SELECTOR, '.header__userzone-control--auth')
user_logo_user_name = (By.CSS_SELECTOR, '.header__userzone-control--auth .header__userzone-label')

company_info_link = (By.CSS_SELECTOR, '.footer__nav a[href="/about-magnit/"]')
contacts_link = (By.CSS_SELECTOR, '.footer__nav a[href="/contacts/"]')
feedback_link = (By.CSS_SELECTOR, '.footer__nav a[href="/feedback/"]')
how_to_order_link = (By.CSS_SELECTOR, '.footer__nav a[href="/how_to_order"]')
payment_link = (By.CSS_SELECTOR, '.footer__nav a[href="/payment"]')
return_link = (By.CSS_SELECTOR, '.footer__nav a[href="/return"]')
promo_rules_link = (By.CSS_SELECTOR, '.footer__nav a[href="/promo-rules"]')
medication_release_link = (By.CSS_SELECTOR, '.footer__row--bottom a[href="/medication_release"]')
politics_personal_data_link = (By.CSS_SELECTOR, '.footer__row--bottom a[href="/politics_personal_data"]')
terms_of_use_link = (By.CSS_SELECTOR, '.footer__row--bottom a[href="/terms_of_use/"]')
legal_information_link = (By.CSS_SELECTOR, '.footer__row--bottom a[href="/legal_information/"]')

big_banners = (By.CSS_SELECTOR, 'div[data-test-id="carouser-banner"]')
second_banner_img = (By.CSS_SELECTOR, 'div[data-test-id="carouser-banner"]:nth-child(2) img')





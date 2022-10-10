from selenium.webdriver.common.by import By

sign_in_button = (By.CLASS_NAME, 'login')
go_to_login_screen_button = (By.CSS_SELECTOR,
                             'div[class="header__userzone-image header__userzone-image--auth"]')
confirm_address_button = (By.CSS_SELECTOR, '.b-location-confirmation .b-location-confirmation__buttons-list button')
login_input = (By.CSS_SELECTOR, 'input[placeholder="Телефон или электронная почта"]')
password_input = (By.CSS_SELECTOR, 'input[placeholder="Пароль"]')
submit_button = (By.CSS_SELECTOR, 'button[data-test-id="button-login"]')
buy_button = (By.CSS_SELECTOR, 'button[data-test-id="product-buy-btn"]')
add_to_favorite_btn = (By.CSS_SELECTOR, 'button[data-test-id="favorite-btn"]')

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
first_banner_img = (By.CSS_SELECTOR, 'div[data-test-id="carouser-banner"]:nth-child(1) img')
second_banner_img = (By.CSS_SELECTOR, 'div[data-test-id="carouser-banner"]:nth-child(2) img')
third_banner_img = (By.CSS_SELECTOR, 'div[data-test-id="carouser-banner"]:nth-child(3) img')
fourth_banner_img = (By.CSS_SELECTOR, 'div[data-test-id="carouser-banner"]:nth-child(4) img')
fifth_banner_img = (By.CSS_SELECTOR, 'div[data-test-id="carouser-banner"]:nth-child(5) img')
next_big_banner_button = (By.CSS_SELECTOR, '.swiper-button-next')
previous_big_banner_button = (By.CSS_SELECTOR, '.swiper-button-prev')

# login_window = (By.XPATH, ".//p[@class='error' and contains(text(),'{0}')]")
login_window = (By.CSS_SELECTOR, ".upblock__wrapper")
home_page = (By.CSS_SELECTOR, '.page-content')
cart_items_counter = (By.CSS_SELECTOR, '.b-counter')

item_carousel_drag_and_drop_from_right_to_left_source = (By.CSS_SELECTOR, 'div.index-page__product-lists '
                                                                          '.b-page-block:nth-child(2) '
                                                                          '.product-list__item:nth-child(4) button['
                                                                          'data-test-id="product-buy-btn"]')
right_item_carousel = (By.CSS_SELECTOR, 'div.index-page__product-lists .b-page-block:nth-child(2) '
                                        '.product-list__item:nth-child(7)')

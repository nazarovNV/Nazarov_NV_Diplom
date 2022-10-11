from selenium.webdriver.common.by import By


pharmacy_input = (By.CSS_SELECTOR, '.b-field__caption')
name_input = (By.CSS_SELECTOR, 'input[data-test-id="input-name"]')
phone_input = (By.CSS_SELECTOR, 'input[data-test-id="input-phone"]')
email_input = (By.CSS_SELECTOR, 'input[data-test-id="input-email"]')
order_number_input = (By.CSS_SELECTOR, 'input[data-test-id="input-order-id"]')
select_pharmacy_button = (By.CSS_SELECTOR, 'button[data-test-id="button-select-pharmacy"]')
select_any_pharmacy_button = (By.CSS_SELECTOR, 'button[data-test-id="button-select"]')
the_text_of_the_appeal_input = (By.CSS_SELECTOR, '.b-field__textarea')
upload_button = (By.CSS_SELECTOR, 'input[data-test-id="button-attach-file"]')
get_answer_operator_call_is_required_radiobutton = (By.CSS_SELECTOR, 'div[data-test-id="section-get-answer"]:nth'
                                                                     '-child(1) input')
get_answer_email_radiobutton = (By.CSS_SELECTOR, 'div[data-test-id="section-get-answer"]:nth-child(2) input')

approval_checkbox = (By.CSS_SELECTOR, 'label[data-test-id="checkbox-policy"] span')

submit_button = (By.CSS_SELECTOR, 'button[data-test-id="button-send"]')

thank_you_for_contacting_us = (By.CSS_SELECTOR, 'div.b-feedback-send__wrapper')
to_the_main_page_button = (By.CSS_SELECTOR, '.b-feedback-send__button')


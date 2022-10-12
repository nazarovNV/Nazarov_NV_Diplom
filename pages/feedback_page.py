import allure
from selenium.common import NoSuchElementException

from pages.locators import feedback_page_locators
from pages.base_page import BasePage


class FeedbackPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_name_input(self):
        with allure.step("Заполнить поле 'Имя'"):
            self.find_element(feedback_page_locators.name_input).send_keys("Имя тест")

    def fill_number_input(self):
        with allure.step("Заполнить поле 'Телефон'"):
            self.find_element(feedback_page_locators.phone_input).send_keys("+79964410394")

    def fill_email_input(self):
        with allure.step("Заполнить поле 'Почта'"):
            self.find_element(feedback_page_locators.email_input).send_keys("test284673092@test.ru")

    def fill_order_number_input(self):
        with allure.step("Заполнить поле 'Номер заказа'"):
            self.find_element(feedback_page_locators.order_number_input).send_keys("115584879")

    def click_pharmacy_button(self):
        with allure.step("Нажать кнопку 'Выбрать аптеку'"):
            self.find_element(feedback_page_locators.select_pharmacy_button).click()

    def click_any_pharmacy_button(self):
        with allure.step("Выбрать первую аптеку"):
            self.find_element(feedback_page_locators.select_any_pharmacy_button).click()

    def fill_text_of_the_appeal_input(self):
        with allure.step("Заполнить поле 'Текст обращения'"):
            self.find_element(feedback_page_locators.the_text_of_the_appeal_input).send_keys("Текст обращения тест")

    def upload_file_png(self):
        with allure.step("Прикрепить png файл"):
            self.find_element(feedback_page_locators.upload_button).send_keys(r"D:\png_test.png")

    def upload_file_jpg(self):
        with allure.step("Прикрепить jpg файл"):
            self.find_element(feedback_page_locators.upload_button).send_keys(r"D:\jpg_test.jpg")

    def upload_file_pdf(self):
        with allure.step("Прикрепить pdf файл"):
            self.find_element(feedback_page_locators.upload_button).send_keys(r"D:\pdf_test.pdf")

    def upload_file_jpeg(self):
        with allure.step("Прикрепить jpeg файл"):
            self.find_element(feedback_page_locators.upload_button).send_keys(r"D:\jpeg_test.jpeg")

    def click_get_answer_email_radiobutton(self):
        with allure.step("Выбрать 'Я хочу получить ответ по электронной почте'"):
            self.find_element(feedback_page_locators.get_answer_email_radiobutton).click()

    def click_approval_checkbox(self):
        with allure.step("Нажать кнопку 'Даю согласие на обработку персональных данных'"):
            self.find_element(feedback_page_locators.approval_checkbox).click()

    def click_submit_button(self):
        with allure.step("Подтвердить отправку формы"):
            self.find_element(feedback_page_locators.submit_button).click()

    def check_is_there_thank_you_for_contacting_us_text(self):
        with allure.step("Проверить видна ли надпись 'Благодарим за обращение!'"):
            try:
                self.is_element_visible(feedback_page_locators.thank_you_for_contacting_us)
            except NoSuchElementException:
                return False
            return True

    def click_to_the_main_page_button(self):
        with allure.step("Нажать кнопку 'На главную страницу'"):
            self.find_element(feedback_page_locators.to_the_main_page_button).click()




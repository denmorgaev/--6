from time import sleep

import allure

from curl import main_page_url
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Дождаться загрузку главной страницы')
    def wait_for_main_page(self):
        self.wait_for_page(main_page_url)

    @allure.step('Дождаться загрузку вопросов')
    def wait_for_questions_list(self):
        self.wait_for_element(MainPageLocators.question_link)

    @allure.step('Открыть вопрос')
    def click_on_question(self, question_number, timeout=10):
        question_locator = MainPageLocators.question_number(question_number)
        self.scroll_to_element(question_locator)
        self.jsclick_on_element(question_locator, timeout)

    @allure.step('Дождаться, пока откроется нужный ответ')
    def wait_for_answer_visible(self, answer_number):
        self.wait_for_element(MainPageLocators.answer_number(answer_number))

    @allure.step('Сравнить ответ вопроса')
    def check_answer_name(self, expected_text, answer_number):
        actual_text = self.get_text_on_element(MainPageLocators.answer_number(answer_number))
        return actual_text == expected_text

    @allure.step('Дождаться перехода на сайт Дзена')
    def redirect_to_dzen(self):
        self.wait_url_change('dzen')

    @allure.step('Нажать на кнопку Заказать вверху сайта')
    def click_the_button_order_on_the_top(self):
        self.click_on_element(MainPageLocators.order_button_on_top)

    @allure.step('Скролл и клик на кнопку Заказать внизу сайта')
    def scroll_and_click_order_button_from_below(self):
        self.scroll_to_element(MainPageLocators.order_button_from_below)
        self.click_on_element(MainPageLocators.order_button_from_below, timeout=50000)

    @allure.step('Нажать на логотип самоката')
    def click_the_scooter_logo(self):
        self.click_on_element(MainPageLocators.scooter_button)

    @allure.step('Нажать на кнопку Яндекса')
    def click_the_yandex_button(self):
        self.click_on_element(MainPageLocators.yandex_button)
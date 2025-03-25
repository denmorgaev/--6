import allure
import pytest

import data

from pages.main_page import MainPage


class TestQuestionAboutImportant:
    @allure.title('При нажатии на вопрос открывается верный ответ к нему')
    @pytest.mark.parametrize('question_number, expected_text', data.Data.questions_names)
    def test_successfully_click_on_question_and_have_right_answer(self, driver, question_number, expected_text):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.wait_for_questions_list()
        main_page.click_on_question(question_number)
        main_page.wait_for_answer_visible(question_number)
        assert main_page.check_answer_name(expected_text, question_number)



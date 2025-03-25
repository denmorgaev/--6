import allure
import pytest
from locators.tabs_questions_locator import QaScooterQuestions as QSQ
from pages.base_page import BasePage
from data.data import Text



class TestClickQuestion:

    @allure.step('Проверка раздела "Вопросы о важном"')
    @pytest.mark.parametrize('answer, tab, text_answer', zip(QSQ.questions, QSQ.tab_answer, Text.text_answer))
    def test_tab_question(self,driver,tab,answer,text_answer):
        tabs_page = BasePage(driver)
        tabs_page.scroll_element(answer)
        tabs_page.click_element(answer)
        text = tabs_page.text_answer(tab)
        assert text == text_answer


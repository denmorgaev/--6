from data.data import Users
from pages.order_page import OrderPage
from locators.order_locator import OrderLocator as OL
from pages.base_page import BasePage
import allure
import pytest

class TestOrder:

    @allure.description('Проверка кнопок "Заказать" и успешный заказ самоката')
    @pytest.mark.parametrize('user, button',zip([Users.user_1, Users.user_2], [OL.button_order,OL.button_order_scroll]))
    def test_order_one(self,driver,user,button):
        page = OrderPage(driver)
        base = BasePage(driver)
        base.scroll_element(button)
        base.click_element(button)
        page.all_fields(user)
        assert page.order_title()


test_question_tab.py
import allure
import pytest

from data import credentials_1, credentials_2
from pages.order_page import OrderPage


class TestMakeAnOrder:
    @allure.title('Оформление заказа')
    @pytest.mark.parametrize('credentials', [credentials_1, credentials_2])
    def test_successful_order(self, driver, credentials):
        order_page = OrderPage(driver)
        order_page.wait_for_order_page()
        order_page.test_successful_completion_of_the_order_form(
            credentials['name'],
            credentials['last_name'],
            credentials['address'],
            credentials['phone_number'],
            credentials['comment']
        )
        order_page.wait_order_created()
        assert order_page.wait_for_find_element()









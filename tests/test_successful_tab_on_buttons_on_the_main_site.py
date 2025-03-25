import allure

from curl import order_page_url, main_page_url
from pages.main_page import MainPage

class TestButtonsOneTheMainPage:
    @allure.title('Нажатие на кнопку Заказать вверху страницы ведет на поле оформления заказа')
    def test_successful_tab_on_the_order_button_on_the_top(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_the_button_order_on_the_top()
        assert main_page.is_current_url(order_page_url)

    @allure.title('Нажатие на кнопку Заказать внизу страницы ведет на поле оформления заказа')
    def test_successful_tab_on_the_order_button_from_below(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.scroll_and_click_order_button_from_below()
        assert main_page.is_current_url(order_page_url)

    @allure.title('Нажатие на логотип Самоката ведет на главную страницу Самоката')
    def test_successful_tab_on_the_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_the_scooter_logo()
        assert main_page.is_current_url(main_page_url)

    @allure.title('Нажатие на логотип Яндекса ведет на страницу Дзена через редирект')
    def test_successful_tab_on_the_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_the_yandex_button()
        main_page.wait_for_two_windows()
        main_page.redirect_to_dzen()
        assert main_page.is_current_url_contains('dzen.ru')
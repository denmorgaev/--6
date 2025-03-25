from pages.base_page import BasePage
from pages.header_page import HeaderPages
from data.data import Urls as U
import allure
class TestHeader:
    @allure.description('Проверка перехода на главную страницу при нажатии на кнопку "Самокат"')
    def test_header_samokat(self,driver):
        header = HeaderPages(driver)
        base = BasePage(driver)
        header.header_button_samokat()
        url = base.current_url()
        assert url == U.main_page

    @allure.description('Проверка перехода на главную страницу "Дзен" при нажатии на кнопку "Яндекс"')
    def test_header_dzen(self,driver):
        header = HeaderPages(driver)
        title = header.header_button_dzen()
        assert title == U.dzen_page
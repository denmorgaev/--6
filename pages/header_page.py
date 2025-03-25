from locators.header_locator import Header
from pages.base_page import BasePage
import allure
class HeaderPages(BasePage):

    @allure.step('Проверка работы кнопки "Самокат"')
    def header_button_samokat(self):
        self.click_element(Header.button_order)
        self.click_element(Header.logo_samokat)

    @allure.step('Переход на страницу "Дзен"')
    def header_button_dzen(self):
        self.click_element(Header.logo_yandex)
        self.new_window()
        self.display_locator(Header.home_dzen)
        return self.current_url()


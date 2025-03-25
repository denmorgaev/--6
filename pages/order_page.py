import allure

from curl import  order_page_url
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    @allure.step('Дождаться загрузку страницы заказа')
    def wait_for_order_page(self):
        self.wait_for_page(order_page_url)
        self.click_on_element(OrderPageLocators.consent_button)

    @allure.title('Заполнение полей ввода на странице заказа самоката')
    def test_successful_completion_of_the_order_form(self, name, last_name, address, phone_number, comment):
        self.send_keys_to_input(OrderPageLocators.name_field, name)
        self.send_keys_to_input(OrderPageLocators.last_name_field, last_name)
        self.send_keys_to_input(OrderPageLocators.address_field, address)
        self.click_on_element(OrderPageLocators.metro_station_field)
        self.scroll_to_element(OrderPageLocators.metro_station_name)
        self.click_on_element(OrderPageLocators.metro_station_name)
        self.send_keys_to_input(OrderPageLocators.telephone_number_field, phone_number)
        self.click_on_element(OrderPageLocators.further_button)
        self.click_on_element(OrderPageLocators.time_to_deliver_field)
        self.click_on_element(OrderPageLocators.date)
        self.click_on_element(OrderPageLocators.days_of_rent)
        self.click_on_element(OrderPageLocators.rent_duration)
        self.click_on_element(OrderPageLocators.comment_field)
        self.send_keys_to_input(OrderPageLocators.comment_field, comment)
        self.click_on_element(OrderPageLocators.order_button_on_page_order)
        self.click_on_element(OrderPageLocators.yes_button)

    @allure.step('Дождаться появление текста элемента')
    def wait_order_created(self):
        self.text_is_visible(OrderPageLocators.order_created, 'Заказ оформлен')

    @allure.step('Дождаться появление кнопки Просмотреть заказ')
    def wait_for_find_element(self):
        self.find_element(OrderPageLocators.see_status_button)











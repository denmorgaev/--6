from locators.order_locator import OrderLocator
import allure
from pages.base_page import BasePage

class OrderPage(BasePage):


    @allure.step('Ввод данных в поле "Имя"')
    def name_order_input(self, text):
        self.click_element(OrderLocator.name)
        self.enter_value(OrderLocator.name, text)

    @allure.step('Ввод данных в поле "Фамилия"')
    def input_last_name(self, text):
        self.enter_value(OrderLocator.last_name, text)

    @allure.step('Ввод данных в поле "Адресс"')
    def input_adress(self, text):
        self.enter_value(OrderLocator.adress, text)

    @allure.step('Ввод данных в поле "Станция метро"')
    def input_metro_station(self):
        self.click_element(OrderLocator.metro_station)
        self.click_element(OrderLocator.station)

    @allure.step('Ввод данных в поле "Телефон"')
    def input_phone(self, text):
        self.enter_value(OrderLocator.phone, text)

    @allure.step('Нажатие кнопки далее')
    def next_window(self):
        self.click_element(OrderLocator.next_button)

    @allure.step('Нажатие по поля "* Когда привезти самокат и выбор даты"')
    def date_field(self):
        self.click_element(OrderLocator.delivery_date)
        self.click_element(OrderLocator.calendar)

    @allure.step('Нажатие по поля "Срок аренды"')
    def rental_period(self):
        self.click_element(OrderLocator.rental)
        self.click_element(OrderLocator.rental_list)

    @allure.step('Выбор цвета самоката')
    def color(self):
        self.click_element(OrderLocator.color_samokat)

    @allure.step('Коментарий для курьера')
    def courier_comment(self,text):
        self.enter_value(OrderLocator.comment_field, text)

    @allure.step('Нажать кнопку "Заказать"')
    def button_order_1(self):
        self.click_element(OrderLocator.order_button)

    @allure.step('Нажать кнопку "Да" в подтверждении заказа')
    def order_confirmation(self):
        self.click_element(OrderLocator.button_yes)

    @allure.step('Отображение окна подтверждения заказа')
    def order_title(self):
        return self.display_locator(OrderLocator.order_confirmed).is_displayed()

    @allure.step('Ввод данных заказа')
    def all_fields(self, data):
        self.name_order_input(data[1])
        self.input_last_name(data[2])
        self.input_adress(data[3])
        self.input_metro_station()
        self.input_phone(data[4])
        self.next_window()
        self.date_field()
        self.rental_period()
        self.color()
        self.courier_comment(data[5])
        self.button_order_1()
        self.order_confirmation()
        self.display_locator(OrderLocator.order_confirmed)






from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    @allure.step('Ожидание текущей страницы')
    def current_url(self):
        url = self.driver.current_url
        return url

    @allure.step('Получение заголовка страницы')
    def page_title(self):
        locator = self.driver.title
        return locator

    @allure.step('Скролл до элемента')
    def scroll_element(self,locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Кликнуть по элементу')
    def click_element(self,locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ожидание локатора')
    def display_locator(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание текста локатора')
    def text_answer(self,locator):
        return self.display_locator(locator).text


    @allure.step('Ввести значение в поле')
    def enter_value(self,locator,data):
        self.driver.find_element(*locator).send_keys(data)

    @allure.step('Обновить страницу')
    def refresh(self,driver):
        driver.refresh()

    @allure.step('Переход на новую страницу')
    def new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
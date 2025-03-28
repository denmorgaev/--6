import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать видимость элемента')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельность элемента')
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    @allure.step('Кликнуть на элемент программно')
    def jsclick_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].click()", element)

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Подождать и проверить, что атрибут элемента содержит текст')
    def wait_for_attribute(self, locator, attribute,  value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(locator, attribute, value))

    @allure.step('Дождаться загрузку страницы')
    def wait_for_page(self, page_url):
        self.driver.get(page_url)

    @allure.step('Дождаться появление текста элемента')
    def text_is_visible(self, locator, text):
        WebDriverWait(self.driver, 100).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Дождаться, пока откроются два окна')
    def wait_for_two_windows(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    @allure.step('Дождаться перехода на сайт Дзена')
    def wait_url_change(self, url, timeout=1000):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))

    @allure.step('Найти элемент на странице')
    def find_element(self, locator, timeout=10):
        self.driver.find_element(locator, timeout)

    @allure.step('Сравнить урл')
    def is_current_url(self, url):
        return self.driver.current_url == url

    @allure.step('Сравнить часть урла')
    def is_current_url_contains(self, url_part):
        return url_part in self.driver.current_url
from selenium.webdriver.common.by import By

class MainPageLocators:
    order_button_on_top = [By.CSS_SELECTOR, '[class^=Header_Nav] button']
    order_button_from_below = [By.CSS_SELECTOR, '[class^=Home_FinishButton] button']
    question_link = [By.CSS_SELECTOR, '[class^=Home_FourPart] [class^=Home_SubHeader]']
    scooter_button = [By.CSS_SELECTOR, '[class^=Header_Logo] [class^=Header_LogoScooter]']
    yandex_button = [By.CSS_SELECTOR, '[class^=Header_Logo] [class^=Header_LogoYandex]']
    page = [By.CSS_SELECTOR, '[class^=Home_FourPart]']

    @staticmethod
    def question_number(question):
        return By.CSS_SELECTOR, f'.accordion .accordion__item:nth-child({question}) .accordion__heading div'

    @staticmethod
    def answer_number(answer):
        return By.CSS_SELECTOR, f'.accordion .accordion__item:nth-child({answer}) .accordion__panel'


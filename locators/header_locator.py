from selenium.webdriver.common.by import By


class Header:

      # Локаторы переходов
      button_order = (By.XPATH, "(.//button[text() = 'Заказать'])")
      logo_samokat = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
      logo_yandex = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
      home_dzen = (By.XPATH, "(.//div[text() = 'Новости'])")
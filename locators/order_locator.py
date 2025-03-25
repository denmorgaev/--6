from selenium.webdriver.common.by import By


class OrderLocator:
    # Первое окно заказа самоката
    button_order = (By.CLASS_NAME, 'Button_Button__ra12g')
    button_order_scroll = (By.XPATH, '//div[@class = "Home_FinishButton__1_cWm"]/button[text() = "Заказать"]')
    name = (By.XPATH, "//input[@placeholder = '* Имя']")
    last_name = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    adress = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    metro_station = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    station = (By.XPATH, ".//div[text() = 'Черкизовская']")
    phone = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text()='Далее']")

    #Второе окно заказа самоката
    delivery_date = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    calendar = (By.XPATH, '//div[contains(text(),"22")]')
    rental = (By.XPATH, '//div[contains(text() , "* Срок аренды")]')
    rental_list = (By.XPATH, '//div[contains(text() , "двое суток")]')
    color_samokat = (By.ID, 'black')
    comment_field = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    button_yes = (By.XPATH, '//button[text()="Да"]')
    order_confirmed = (By.XPATH, ".//div[text() = 'Заказ оформлен']")

    #Скролл до кнопки заказать
    scroll = (By.XPATH, ".//div[text() = 'Когда аренда заканчивается']")
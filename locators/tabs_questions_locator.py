from selenium.webdriver.common.by import By


class QaScooterQuestions:

    # Локаторы кнопок блока "Вопросы о важном"
    questions = [
        (By.ID, 'accordion__heading-0'),
        (By.ID, 'accordion__heading-1'),
        (By.ID, 'accordion__heading-2'),
        (By.ID, 'accordion__heading-3'),
        (By.ID, 'accordion__heading-4'),
        (By.ID, 'accordion__heading-5'),
        (By.ID, 'accordion__heading-6'),
        (By.ID, 'accordion__heading-7')
    ]

    # Локаторы ответов блока "Вопросы о важном"
    tab_answer = [
        (By.XPATH, '//p[contains(text() , "Сутки — 400 рублей")]'),
        (By.XPATH, '//p[contains(text(),  "один заказ — один самокат")]'),
        (By.XPATH, '//p[contains(text(), "вы оформляете заказ на 8 мая")]'),
        (By.XPATH, '//p[contains(text(), "Только начиная с завтрашнего дня")]'),
        (By.XPATH, '//p[contains(text(), "Пока что нет!")]'),
        (By.XPATH, '//p[contains(text(), "Самокат приезжает к вам с полной зарядкой")]'),
        (By.XPATH, '//p[contains(text(), "Да, пока самокат не привезли")]'),
        (By.XPATH, '//p[contains(text(), "Да, обязательно")]')
    ]


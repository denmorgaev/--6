## <span style="color:MediumPurple">Проект по автоматизации UI-тестов для сервиса **«Яндекс Самокат»**</span> 
`https://qa-scooter.praktikum-services.ru/` 

#### Курс по автоматизации тестирования на Python, «Яндекс Практикум»
#### Спринт 6, Page Object Model

---
### <span style="color:DarkOrchid">Введение в проект</span>
«Яндекс Самокат» — это сервис для аренды самокатов в Москве и Московской области. Приложение создано специально для отработки навыков студентов «Практикума».
Автотесты работают на базе pytest и Selenium и выстроены в соответствии с Page Object Model. Отчет о тестировании генерируется с помощью фреймворка Allure и библиотеки allure-pytest.


### <span style="color:Brown">Запуск всех тестов</span>

Установка зависимостей: `pip install -r requirements.txt`.

Команда для терминала, запускающая все тесты: `pytest -v`.


### <span style="color:IndianRed">Отчет о тестировании</span>

Allure-отчет в формате веб-страницы генерируется командой `allure serve allure_results`.
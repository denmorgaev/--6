import pytest
from selenium import webdriver
from data.data import Urls as U

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(U.main_page)
    yield driver
    driver.quit()

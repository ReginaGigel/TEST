import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login(browser):
    browser.get("https://krasnoyarsk.24ff.ru/")

    login_link = browser.find_element(By.CLASS_NAME,'symbol-login ')
    login_link.click()

    time.sleep(2)

    username_input = browser.find_element(By.NAME, 'phone')
    password_input = browser.find_element(By.NAME, 'password')

    username_input.send_keys("9504021279")
    password_input.send_keys("gigel1912")

    vhod = browser.find_element(By.CLASS_NAME, 'btn-bright-blue')
    vhod.click()
    time.sleep(7)

# Проверка успешности теста
    search_results = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper")
    assert search_results.is_displayed(), "Тест не пройден: результаты входа в аккаунт не отображены"
    print("Тест успешно пройден: результаты  входа в аккаунт отображены")

    browser.quit()
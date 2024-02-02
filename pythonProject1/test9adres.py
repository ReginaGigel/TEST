import pytest
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

    # Находим ссылку для входа в учетную запись и нажимаем на нее
    login_link = browser.find_element(By.CLASS_NAME,'symbol-login ')
    login_link.click()

    time.sleep(2)

    # Заполняем форму логина и пароля
    username_input = browser.find_element(By.NAME, 'phone')
    password_input = browser.find_element(By.NAME, 'password')

    username_input.send_keys("9504021279")
    password_input.send_keys("gigel1912")

    # Отправляем форму для входа
    password_input.send_keys(Keys.RETURN)
    time.sleep(3)

    browser.get("https://krasnoyarsk.24ff.ru/profile")
    time.sleep(2)

    usernamee_input = browser.find_element(By.NAME, 'city')
    passwordd_input = browser.find_element(By.NAME, 'street')
    passworddd_input = browser.find_element(By.NAME, 'house')

    usernamee_input.send_keys("Красноярск")
    passwordd_input.send_keys("Весны")
    passworddd_input.send_keys("1")
    button = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main > div:nth-child(3) > div > div.col-xxl-9.col-md-8.col-sm-12 > div > div.form-section > div.js-address-container > form > div > div.spoiler-content.js-spoiler-content > div > div.col-xxl-6.col-sm-12").click()
    time.sleep(4)


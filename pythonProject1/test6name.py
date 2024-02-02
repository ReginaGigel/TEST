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

    password_input.send_keys(Keys.RETURN)
    time.sleep(3)

    browser.get("https://krasnoyarsk.24ff.ru/profile")
    time.sleep(2)

    username1_input = browser.find_element(By.NAME, 'name')
    birthday_input = browser.find_element(By.NAME, 'birthday')

    username1_input.send_keys("Регина")
    birthday_input.send_keys("19122000")
    birthday_input.send_keys(Keys.RETURN)
    time.sleep(3)

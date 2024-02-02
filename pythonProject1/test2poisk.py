from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://krasnoyarsk.24ff.ru/"
browser = webdriver.Chrome()
browser.get(link)
s_string = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > button > svg").click()
search_string = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > div > input[type=text]")
time.sleep(3)
search_string.send_keys("D3")
button_poisk = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > button > svg").click()
time.sleep(3)

# Проверка успешности теста
search_results = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper")
assert search_results.is_displayed(), "Тест не пройден: результаты поиска не отображены"
print("Тест успешно пройден: результаты поиска отображены")

browser.quit()
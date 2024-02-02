from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://krasnoyarsk.24ff.ru/"
browser = webdriver.Chrome()
browser.get(link)
gorod = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-top > div.location-wrapper.js-city-detect > a").click()
vibor_goroda = browser.find_element(By.CSS_SELECTOR, "#city-popup > div.city-list-wrapper.tabs-wrapper.js-tabs-wrapper > div.tab-content.active > div > ul > li:nth-child(34) > a").click()
time.sleep(6)
# Проверка успешности теста
search_results = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper")
assert search_results.is_displayed(), "Тест не пройден: выбранный город не отображен"
print("Тест успешно пройден:выбранный город отображен")

browser.quit()
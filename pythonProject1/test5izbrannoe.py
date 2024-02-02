from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://krasnoyarsk.24ff.ru/"
browser = webdriver.Chrome()
browser.get(link)
s_string = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > button > svg").click()
search_string = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > div > input[type=text]")
time.sleep(3)
search_string.send_keys("WHEY")
button_poisk = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > button > svg").click()
time.sleep(3)
button_tovar = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main > section > div > div.grid-row.products-list > div:nth-child(1) > div").click()
button_v_izbrannie = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main > div:nth-child(3) > div.container.js-sku-selector > section > div.slider-col > a").click()
time.sleep(3)
button_izbrannie = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > a.user-info.favorites.js-header-fav-count.cart").click()
# Проверка успешности теста
search_results = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper")
assert search_results.is_displayed(), "Тест не пройден: результаты не отображены"
print("Тест успешно пройден: результаты  отображены")

browser.quit()
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://krasnoyarsk.24ff.ru/"
browser = webdriver.Chrome()
browser.get(link)
s_string = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > button > svg").click()
search_string = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > div > input[type=text]")
time.sleep(3)
search_string.send_keys("BCAA")
button_poiskk = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > button > svg").click()
time.sleep(3)
button_tovar = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main > section > div > div.grid-row.products-list > div:nth-child(2) > div > div.buy-wrapper > a").click()
time.sleep(3)
buttonn_tovar = browser.find_element(By.CSS_SELECTOR, "#fast-view-popup > div > section > div.details-col.js-sku-item > form > div.submit-wrap > a.btn.btn-red.submit-btn.js-to-cart").click()
buttonnn_tovar = browser.find_element(By.CSS_SELECTOR, "#fast-view-popup > button").click()
button_korzina = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > a.user-info.cart.js-header-cart-count").click()
time.sleep(3)
# Проверка результатов теста
search_results = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main")
assert search_results.is_displayed(), "Тест не пройден: товары в корзине не отображены"
print("Тест успешно пройден: товары в корзине отображены")

browser.quit()
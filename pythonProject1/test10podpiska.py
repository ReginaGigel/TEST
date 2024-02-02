from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://krasnoyarsk.24ff.ru/"
browser = webdriver.Chrome()
browser.get(link)
s_string = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > button > svg").click()
search_string = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > div > input[type=text]")
time.sleep(3)
search_string.send_keys("Glutamine")
poisk = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > div.user-info-wrapper > form > button > svg").click()
time.sleep(3)
tovar = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main > section > div > div.grid-row.products-list > div:nth-child(1) > div").click()
time.sleep(3)
email_input = browser.find_element(By.NAME, 'email')
email_input.send_keys("gigelina@mail.ru")
time.sleep(4)
soglasie = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main > div:nth-child(3) > div.container.js-sku-selector > div > div > div:nth-child(1) > form > div.policy-checkbox-wrap > label > span").click()
time.sleep(3)
podpiska= browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main > div:nth-child(3) > div.container.js-sku-selector > div > div > div:nth-child(1) > form > button").click()
time.sleep(5)
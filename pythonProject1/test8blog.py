from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://krasnoyarsk.24ff.ru/"
browser = webdriver.Chrome()
browser.get(link)
blog = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > div.header-wrapper > header > div > div.header-row.header-row-bottom.js-menu > nav > div:nth-child(7) > a").click()
time.sleep(3)
recepti = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main > div:nth-child(3) > form > div > label:nth-child(5) > span").click()
time.sleep(4)
slatya = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main > div:nth-child(3) > div > div > div > div > div").click()
time.sleep(4)
browser.get("https://krasnoyarsk.24ff.ru/blog/kak-prigotovit-proteinovyj-koktejl-dlya-veganov")
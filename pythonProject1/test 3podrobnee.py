from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://krasnoyarsk.24ff.ru/"
browser = webdriver.Chrome()
browser.get(link)
podronee = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > main > div.main-promo-wrapper.js-main-promo-block > div > div.swiper-container.main-promo-slider-front.swiper-container-initialized.swiper-container-horizontal.top-at-bottom > div > div.swiper-slide.slide.swiper-no-swiping.swiper-slide-visible.swiper-slide-active.swiper-slide-duplicate-next.swiper-slide-duplicate-prev > div.product-info > a").click()
time.sleep(7)

# Проверка успешности теста
search_results = browser.find_element(By.CSS_SELECTOR, "body > div.page-wrapper")
assert search_results.is_displayed(), "Тест не пройден: результаты не отображены"
print("Тест успешно пройден: результаты  отображены")

browser.quit()
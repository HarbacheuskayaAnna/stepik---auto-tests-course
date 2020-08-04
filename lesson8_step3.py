from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ваш код, который заполняет обязательные поля
    summ: int = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
    print(summ)
    select_in_list = Select(browser.find_element_by_tag_name("select"))
    select_in_list.select_by_visible_text(str(summ))
    btn = browser.find_element_by_tag_name("button")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    chb = browser.find_element_by_id("robotCheckbox")
    chb.click()
    browser.execute_script("window.scrollBy(0, 100);")
    rdb = browser.find_element_by_id("robotsRule")
    rdb.click()
    btn = browser.find_element_by_tag_name("button")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
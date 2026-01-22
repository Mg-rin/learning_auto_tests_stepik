import time, math, os
from selenium.webdriver.common.by import By


def test_modul_23_step2(browser):
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    try:
        link = "http://suninjuly.github.io/redirect_accept.html"

        browser.get("http://suninjuly.github.io/redirect_accept.html")
        browser.find_element(By.CSS_SELECTOR, "button.trollface").submit()

        browser.switch_to.window(browser.window_handles[1])

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        print(x)
        y = calc(x) # вычисление х
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.CSS_SELECTOR, "button.btn").submit()


    finally:
        print(browser.switch_to.alert.text)
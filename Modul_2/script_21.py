import time, math, os, pytest
from selenium.webdriver.common.by import By


def test_modul_21_step1(browser):
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser.get("https://suninjuly.github.io/math.html")
    time.sleep(5)

    x_element = browser.find_element(By.CSS_SELECTOR, "form-control")
    x = x_element.text
    y = calc(x)
    x_element.send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "form-check-input").click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "submit").click()

def test_modul_21_step2(browser):
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.get("https://suninjuly.github.io/math.html")

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

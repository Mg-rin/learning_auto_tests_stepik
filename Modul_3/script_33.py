from selenium import webdriver
from selenium.webdriver.common.by import By

#pytest script_33.py

def test_form_registration1():

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    # заполняем обязательные поля (только first_block)
    browser.find_element(By.CSS_SELECTOR, ".form-control.first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".form-control.second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".form-control.third").send_keys("test@example.com")
    # отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # проверяем успешную регистрацию
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!"




def test_form_registration2(self):
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    # заполняем обязательные поля (только first_block)
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("test@example.com")
    # отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # проверяем успешную регистрацию
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!"


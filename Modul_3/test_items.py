import pytest, time, math
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_guest_should_see_login_link(browser, pytestconfig):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    language = pytestconfig.getoption("--language")

    time.sleep(10)
    if language == "es":
        correct_text = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").text
        assert correct_text == "Añadir al carrito"
        print("Нашел и перевел")

    else:
        #with pytest.raises(NoSuchElementException):  # проверка на наличие элемента
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        print("Нашел!") #  pytest --language=ru -s test_items.py

            #pytest.fail("не Найден!")




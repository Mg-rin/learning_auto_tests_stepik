from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, pytest

#инициализация драйвера в файле conftest из 3.6 step 6
def test_modul_16_step_4(browser):

    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser.get(link)

    text = str(math.ceil(math.pow(math.pi, math.e) * 10000)) # step
    link = browser.find_element(By.LINK_TEXT, text)
    link.click()

    # 1.6 step 4 поиск элементов с помощью Selenium
    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


# find_element(By.ID, value) — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
# find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
# find_element(By.XPATH, value) — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
# find_element(By.NAME, value) — поиск по атрибуту name элемента;
# find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента;
# find_element(By.CLASS_NAME, value) — поиск по значению атрибута class;
# find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
# find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.

def test_modul_16_step4(browser):
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

def test_modul_16_step5(browser):
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.XPATH, '//button [text() = "Submit"]')
    button.click()

def test_modul_16_step6(browser):
    browser.get("http://suninjuly.github.io/registration2.html")

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CLASS_NAME, "first").send_keys("Ivan")
    browser.find_element(By.CLASS_NAME, "second").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "third").send_keys("rina.@gmail.com")
    div = browser.find_element(By.XPATH, "//div[@class='second_block']")
    div.find_element(By.CLASS_NAME, "first").send_keys("89900898909")
    div.find_element(By.CLASS_NAME, "second").send_keys("Smolensk, dfgfg fhgfgyt 34")

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
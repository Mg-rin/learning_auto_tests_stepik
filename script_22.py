import time, math, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_modul_22_step1(browser):

    link = "https://suninjuly.github.io/selects1.html"
    browser.get(link)
    select = Select(browser.find_element(By.ID, "dropdown"))

    summ = int((browser.find_element(By.ID, "num1")).text) + int((browser.find_element(By.ID, "num2")).text)
    time.sleep(2)
    select.select_by_visible_text(str(summ))
    # print(str(summ))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

def test_modul_22_step2(browser):
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)  # открытие страницы

    x_element = browser.find_element(By.ID, "input_value")  # считывание переменной х
    x = x_element.text
    y = calc(x)  # вычисление х
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           browser.find_element(By.CSS_SELECTOR, "button.btn"))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").submit()


def test_modul_22_step3(browser):
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Иван")
    browser.find_element(By.NAME, "lastname").send_keys("Иванов")
    browser.find_element(By.NAME, "email").send_keys("em@.ru")

    dirr = os.path.abspath(os.path.dirname(__file__))  # расположение исполняемого файла
    print(dirr)
    browser.find_element(By.NAME, "file").send_keys(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), 'down.txt'))
    browser.find_element(By.CSS_SELECTOR, "button.btn").submit()
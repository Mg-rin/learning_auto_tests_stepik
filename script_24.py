from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math, os

# try:
#     link = "http://suninjuly.github.io/cats.html"
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(5)
#     browser.get(link)
#
#     browser.find_element(By.ID, "button")
#
# finally:
#     browser.quit()

browser = webdriver.Chrome()
#browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    wait = WebDriverWait(browser,12)
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    y = calc(x) # вычисление х
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").submit()

    # wait.until(
    #     EC.element_to_be_clickable((By.ID, "book"))
    # )


# except TimeoutException:
#     print("Не нашел")


finally:
    time.sleep(10)
    browser.quit()
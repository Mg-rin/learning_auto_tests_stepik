import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options() #3.6 step 9 Запуск автотестов для разных языков интерфейса

def pytest_addoption(parser): #3.6 step 6 передача параметров в командной строке
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox") # pytest -s -v --browser_name=firefox file.py
    parser.addoption('--reruns n') #n — это количество перезапусков
    parser.addoption('--tb=line')



@pytest.fixture(scope="function") #
def browser(request):

    #user_language = request.config.getoption("user_language") #3.6 step 9 Запуск автотестов для разных языков интерфейса
    browser_name = request.config.getoption("browser_name")  # 3.6 step 6

    #options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) #3.6 step 9 Запуск автотестов для разных языков интерфейса

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)  # неявное ожидание вместо sleep
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        browser.implicitly_wait(10)  # неявное ожидание вместо sleep
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
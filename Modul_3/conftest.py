import pytest, time
from pygments.lexer import default
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options() #3.6 step 9 Запуск автотестов для разных языков интерфейса

def pytest_addoption(parser): #3.6 step 6 передача параметров в командной строке
    parser.addoption('--language', action = 'store', default = 'ru')



@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")#3.6 step 9 Запуск автотестов для разных языков интерфейса
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    #pytest --language=es test_items.py

    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(10)  # неявное ожидание вместо sleep
    yield browser
    print("\nquit browser..")
    browser.quit()

    return


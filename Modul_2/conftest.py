import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function") #
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)  # неявное ожидание вместо sleep
    yield browser
    print("\nquit browser..")
    browser.quit()
import pytest, time, math
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('page', ["236895", "236896","236897","236898","236899" ,"236903", "236904", "236905"])
#@pytest.mark.parametrize('page', ["236899", "236904"])
def test_guest_should_see_login_link(browser,page):

    link = f"https://stepik.org/lesson/{page}/step/1"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "#ember499").click()
    browser.find_element(By.ID, "id_login_email").send_keys("7@gmail.com")
    browser.find_element(By.ID, "id_login_password").send_keys("pTgfdgfdgsdsdR")
    browser.find_element(By.CSS_SELECTOR,"button.sign-form__btn").click()

    try:
        answer = math.log(int(time.time())) #значение вводимое в поле
        browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area").clear()
        browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area").send_keys(answer)


        with pytest.raises(NoSuchElementException): # проверка на наличие элемента
            #WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
            browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
            pytest.fail("disabled")

    finally: pass

    correct_text = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    assert correct_text == "Correct!"

    print(f"адрес и результат:{browser.current_url} {correct_text}")

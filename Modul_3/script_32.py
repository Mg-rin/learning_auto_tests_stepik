from symtable import Class
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


# def test_input_text(expected_result, actual_result):
#     assert expected_result == actual_result
#     f"{expected_result} соответствует {actual_result}"
#
#
# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
#
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("All tests passed!")

# с использованием unittest 3.2 step 12

# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#     unittest.main()

# 3.2 step 13


class TestStudy(unittest.TestCase):

    def test_form_registration1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        # заполняем обязательные поля (только first_block)
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("test@example.com")
        # отправляем форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        # проверяем успешную регистрацию
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        print(welcome_text)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")



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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)




if __name__ == "__main__":
    unittest.main()


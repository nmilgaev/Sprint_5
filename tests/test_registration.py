from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    NAME_INPUT_FIELD,
    EMAIL_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    REGISTER_BUTTON,
    REGISTER_ERROR,
    LOGIN_HEADER
)
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://stellarburgers.nomoreparties.site/register')


driver.find_element(*NAME_INPUT_FIELD).send_keys("Имятест1")
driver.find_element(*EMAIL_INPUT_FIELD).send_keys("testmai_3@gmail.com")
driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("1244")
driver.find_element(*REGISTER_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(REGISTER_ERROR))

error_message = driver.find_element(*REGISTER_ERROR).text
assert error_message == 'Некорректный пароль'

driver.refresh()

driver.find_element(*NAME_INPUT_FIELD).send_keys("Тест")
driver.find_element(*EMAIL_INPUT_FIELD).send_keys("gw3fjwg44k3w46@gmail.com")
driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("12323433344")
driver.find_element(*REGISTER_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_HEADER))

login_header = driver.find_element(*LOGIN_HEADER).text
assert login_header == 'Вход'
driver.quit()
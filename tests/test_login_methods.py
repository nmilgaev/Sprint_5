from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    USERNAME_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    LOGIN_TO_ACCOUNT_BUTTON,
    PLACE_AN_ORDER,
    PERSONAL_CABINET_LINK,
    LOGOUT_BUTTON,
    REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON
)

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://stellarburgers.nomoreparties.site/')
driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()
driver.find_element(*USERNAME_INPUT_FIELD).send_keys("nikita_milgaev14494@gmail.com")
driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("gowgJGSOSE3")
driver.find_element(*LOGIN_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
login_header = driver.find_element(*PLACE_AN_ORDER).text
assert login_header == 'Оформить заказ'
driver.find_element(*PERSONAL_CABINET_LINK).click()
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LOGOUT_BUTTON))
driver.find_element(*LOGOUT_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_BUTTON))

driver.get('https://stellarburgers.nomoreparties.site/')
driver.find_element(*PERSONAL_CABINET_LINK).click()
driver.find_element(*USERNAME_INPUT_FIELD).send_keys("nikita_milgaev14494@gmail.com")
driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("gowgJGSOSE3")
driver.find_element(*LOGIN_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
login_header = driver.find_element(*PLACE_AN_ORDER).text
assert login_header == 'Оформить заказ'
driver.find_element(*PERSONAL_CABINET_LINK).click()
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LOGOUT_BUTTON))
driver.find_element(*LOGOUT_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_BUTTON))

driver.get('https://stellarburgers.nomoreparties.site/register')
driver.find_element(*REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON).click()
driver.find_element(*USERNAME_INPUT_FIELD).send_keys("nikita_milgaev14494@gmail.com")
driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("gowgJGSOSE3")
driver.find_element(*LOGIN_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
login_header = driver.find_element(*PLACE_AN_ORDER).text
assert login_header == 'Оформить заказ'
driver.find_element(*PERSONAL_CABINET_LINK).click()
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LOGOUT_BUTTON))
driver.find_element(*LOGOUT_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_BUTTON))

driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
driver.find_element(*REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON).click()
driver.find_element(*USERNAME_INPUT_FIELD).send_keys("nikita_milgaev14494@gmail.com")
driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("gowgJGSOSE3")
driver.find_element(*LOGIN_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
login_header = driver.find_element(*PLACE_AN_ORDER).text
assert login_header == 'Оформить заказ'
driver.find_element(*PERSONAL_CABINET_LINK).click()
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LOGOUT_BUTTON))
driver.find_element(*LOGOUT_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_BUTTON))

driver.quit()


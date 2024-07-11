import time
import allure
import pytest
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


scenarios('../features/login_facebook.feature')


@allure.feature("Login")
@allure.story("Tester Login pour Facebook")
@given("l\'utilisateur est sur la page de connexion Facebook")
@allure.step("l'utilisateur est sur la page de connexion Facebook")
def user_on_login_page(driver):
    driver.get('https://www.facebook.com/')
    time.sleep(2)

@when("l\'utilisateur saisit des informations d\'identification non valides")
@allure.step("l'utilisateur saisit des informations d'identification non valides")
def enter_credentials(driver):
    xpath_username = "//html[@id='facebook']//input[@id='email']"
    username_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_username)))
    username_locator.send_keys("oumaymas@ymail.com")
    time.sleep(2)
    xpath_password = "//html[@id='facebook']//input[@id='pass']"
    password_locator = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_password)))
    password_locator.send_keys("123154")
    time.sleep(2)

@when("l\'utilisateur clique sur le bouton de connexion")
@allure.step("l'utilisateur clique sur le bouton de connexion")
def connexion_click(driver):
    submit_button_locator = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By..CSS_SELECTOR, "button[name='login']")))
    submit_button_locator.click()

@then("l\'utilisateur devrait voir un message d\'erreur")
@allure.step("l'utilisateur devrait voir un message d'erreur")
def error_message(driver):
       WebDriverWait(browser, 40).until(
        EC.visibility_of_element_located((By.XPATH, "//html[@id='facebook']//div[@id='loginform']//div[@class='_9ay7'][contains(text(), 'The password you’ve entered is incorrect.')]"))
    )





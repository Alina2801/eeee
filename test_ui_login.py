import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Инициализируем WebDriver (например, для Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_ui_login_success(driver):
    # Открываем страницу авторизации
    driver.get("https://geeks-online.geekstudio.kg/login")

    # Явное ожидание видимости полей логина и пароля
    login_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "login"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )

    # Вводим данные
    login_field.send_keys("Daniyar")
    password_field.send_keys("admin")

    # Ищем и нажимаем кнопку входа
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    login_button.click()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_ui_login_failure(driver):
    
    driver.get("https://geeks-online.geekstudio.kg/login")

    
    login_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "login"))
    )
    password_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )

    
    login_field.send_keys("")
    password_field.send_keys("admin11111")

    
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    login_button.click()

    

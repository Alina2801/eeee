import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Инициализируем WebDriver (например, для Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

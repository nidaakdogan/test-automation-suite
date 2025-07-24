import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'yanlis_sifre')
    error = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
    assert 'Epic sadface' in error.text 
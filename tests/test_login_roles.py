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

def test_locked_out_user_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('locked_out_user', 'secret_sauce')
    error = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
    assert 'locked out' in error.text.lower()

def test_problem_user_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('problem_user', 'secret_sauce')
    assert 'inventory' in driver.current_url 
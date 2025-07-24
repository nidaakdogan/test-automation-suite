import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    assert 'inventory' in driver.current_url 
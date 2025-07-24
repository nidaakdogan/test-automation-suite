import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # Menü butonuna tıkla
    menu_btn = driver.find_element(By.ID, 'react-burger-menu-btn')
    menu_btn.click()
    time.sleep(1)  # Menü animasyonu için kısa bekleme
    # Logout butonuna tıkla
    logout_btn = driver.find_element(By.ID, 'logout_sidebar_link')
    logout_btn.click()
    # Login sayfasına yönlendirildiğini kontrol et
    assert 'saucedemo.com' in driver.current_url and 'login' in driver.page_source.lower() 
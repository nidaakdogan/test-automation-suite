import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_homepage_load_time(driver):
    start = time.time()
    login_page = LoginPage(driver)
    login_page.load()
    load_time = time.time() - start
    assert load_time < 5, f"Sayfa yüklenme süresi çok uzun: {load_time:.2f} sn" 
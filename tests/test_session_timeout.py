import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_session_timeout(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # Oturum açıldıktan sonra 30 saniye bekle (demo site için kısa tuttuk)
    time.sleep(30)
    # Hala ürünler sayfasında mıyız kontrol et
    assert 'inventory' in driver.current_url 
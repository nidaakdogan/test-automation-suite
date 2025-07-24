# Not: Bu test demo/örnek amaçlıdır, gerçek ortamda çalışmayabilir.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_password_reset_example(driver):
    driver.get('http://automationpractice.com/index.php?controller=password')
    # E-posta girip şifre sıfırlama isteği gönder
    email = 'testuser@mail.com'
    driver.find_element(By.ID, 'email').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, 'button.button-medium').click()
    # Başarı/hata mesajı kontrolü
    alert = driver.find_element(By.CSS_SELECTOR, '.alert')
    assert 'email' in alert.text.lower() 
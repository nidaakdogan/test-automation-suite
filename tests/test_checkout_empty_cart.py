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

def test_checkout_with_empty_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # Sepete git
    cart_link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_link.click()
    # Sepet boşken checkout butonuna bas
    checkout_btn = driver.find_element(By.ID, 'checkout')
    checkout_btn.click()
    # Checkout sayfasında olduğumuzu kontrol et (hata mesajı beklenmiyor, sadece checkout sayfasına geçiş olur)
    assert 'checkout-step-one' in driver.current_url 
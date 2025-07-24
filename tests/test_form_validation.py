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

def test_checkout_form_validation(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # Ürün ekle
    add_to_cart_btn = driver.find_element(By.CSS_SELECTOR, '.inventory_item button')
    add_to_cart_btn.click()
    # Sepete git
    cart_link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_link.click()
    # Checkout başlat
    checkout_btn = driver.find_element(By.ID, 'checkout')
    checkout_btn.click()
    # Zorunlu alanları boş bırakıp devam et
    driver.find_element(By.ID, 'continue').click()
    # Hata mesajı kontrolü
    error = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
    assert 'Error' in error.text 
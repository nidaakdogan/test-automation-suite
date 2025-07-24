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

def test_successful_checkout(driver):
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
    # Kullanıcı bilgilerini doldur
    driver.find_element(By.ID, 'first-name').send_keys('Test')
    driver.find_element(By.ID, 'last-name').send_keys('User')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')
    driver.find_element(By.ID, 'continue').click()
    # Siparişi tamamla
    driver.find_element(By.ID, 'finish').click()
    # Başarılı sipariş mesajı kontrolü
    complete_header = driver.find_element(By.CLASS_NAME, 'complete-header')
    assert 'thank you for your order' in complete_header.text.lower() 
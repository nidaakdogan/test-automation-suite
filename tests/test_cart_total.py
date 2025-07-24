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

def test_cart_total_price(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # İlk iki ürünü sepete ekle
    add_buttons = driver.find_elements(By.CSS_SELECTOR, '.inventory_item button')[:2]
    for btn in add_buttons:
        btn.click()
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
    # Ürün fiyatlarını topla
    prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    total_expected = sum(float(p.text.replace('$', '').replace(',', '.')) for p in prices)
    # Ara toplamı kontrol et
    item_total = driver.find_element(By.CLASS_NAME, 'summary_subtotal_label').text
    item_total_value = float(item_total.split('$')[1].replace(',', '.'))
    assert abs(total_expected - item_total_value) < 0.01 
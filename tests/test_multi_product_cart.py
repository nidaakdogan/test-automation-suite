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

def test_multi_product_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # İlk üç ürünü sepete ekle
    add_buttons = driver.find_elements(By.CSS_SELECTOR, '.inventory_item button')[:3]
    for btn in add_buttons:
        btn.click()
    # Sepet ikonundaki sayı kontrolü (3 olmalı)
    cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == '3'
    # Sepete git
    cart_link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_link.click()
    # İlk ürünü sepetten çıkar
    remove_btn = driver.find_element(By.CSS_SELECTOR, '.cart_item button')
    remove_btn.click()
    # Sepette kalan ürün sayısı kontrolü (2 olmalı)
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    assert len(cart_items) == 2
    # Bir ürün daha ekle (geri dönüp ekle)
    driver.find_element(By.ID, 'continue-shopping').click()
    add_buttons = driver.find_elements(By.CSS_SELECTOR, '.inventory_item button')
    for btn in add_buttons:
        if btn.text.lower() == 'add to cart':
            btn.click()
            break
    # Sepete git ve ürün sayısını tekrar kontrol et (3 olmalı)
    cart_link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_link.click()
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    assert len(cart_items) == 3 
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

def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # İlk ürünü sepete ekle
    add_to_cart_btn = driver.find_element(By.CSS_SELECTOR, '.inventory_item button')
    add_to_cart_btn.click()
    # Sepet ikonundaki sayı kontrolü
    cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == '1' 
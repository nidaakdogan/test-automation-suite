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

def test_remove_product_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # İlk ürünü sepete ekle
    add_to_cart_btn = driver.find_element(By.CSS_SELECTOR, '.inventory_item button')
    add_to_cart_btn.click()
    # Sepete git
    cart_link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_link.click()
    # Ürünü sepetten çıkar
    remove_btn = driver.find_element(By.CSS_SELECTOR, '.cart_item button')
    remove_btn.click()
    # Sepetin boş olduğunu kontrol et
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    assert len(cart_items) == 0 
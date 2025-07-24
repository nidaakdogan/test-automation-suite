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

def test_discounted_product_price(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # İlk ürünü sepete ekle
    first_product = driver.find_element(By.CLASS_NAME, 'inventory_item')
    price_text = first_product.find_element(By.CLASS_NAME, 'inventory_item_price').text
    price = float(price_text.replace('$', '').replace(',', '.'))
    first_product.find_element(By.TAG_NAME, 'button').click()
    # Sepete git
    cart_link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_link.click()
    # Sepette fiyatı kontrol et
    cart_price_text = driver.find_element(By.CLASS_NAME, 'inventory_item_price').text
    cart_price = float(cart_price_text.replace('$', '').replace(',', '.'))
    assert price == cart_price 
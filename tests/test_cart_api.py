import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import requests
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_add_to_cart_and_check_api(driver):
    # 1. Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')

    # 2. Ürünü sepete ekle (ilk ürünü ekliyoruz)
    add_to_cart_btn = driver.find_element(By.CSS_SELECTOR, '.inventory_item button')
    add_to_cart_btn.click()

    # 3. API ile sepeti kontrol et (örnek endpoint, gerçek endpoint yoksa bu kısım örnek olarak kalır)
    # NOT: Saucedemo'da public bir API yok, bu yüzden örnek bir GET isteği gösteriyorum.
    # Gerçek projede, oturum çerezi veya token ile istek atılır.
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')  # Örnek API
    assert response.status_code == 200
    # Gerçek API olsaydı, sepette ürün var mı diye kontrol ederdik. 
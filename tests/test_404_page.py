import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_404_page(driver):
    # Saucedemo'da geçersiz ürün URL'sine git
    driver.get('https://www.saucedemo.com/inventory-item.html?id=9999')
    # Hata mesajı veya 404 sayfası kontrolü (saucedemo'da "Epic sadface" hatası çıkar)
    error = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
    assert 'Epic sadface' in error.text 
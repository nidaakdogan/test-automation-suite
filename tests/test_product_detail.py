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

def test_product_detail_page(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # Ürün listesinden ilk ürüne tıkla
    first_product = driver.find_element(By.CLASS_NAME, 'inventory_item_name')
    product_name = first_product.text
    first_product.click()
    # Detay sayfasında ürün adını kontrol et
    detail_name = driver.find_element(By.CLASS_NAME, 'inventory_details_name')
    assert product_name == detail_name.text 
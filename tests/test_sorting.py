import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_sort_products_by_price_asc(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # Sıralama dropdown'unu bul ve fiyata göre artan sırala
    sort_select = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    sort_select.select_by_value('lohi')
    # Ürün fiyatlarını sırayla al
    prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    price_values = [float(p.text.replace('$', '').replace(',', '.')) for p in prices]
    assert price_values == sorted(price_values) 
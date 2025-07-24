import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import requests

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_product_images_and_links(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')
    # Ürün görsellerini kontrol et
    images = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_img img')
    for img in images:
        src = img.get_attribute('src')
        resp = requests.get(src)
        assert resp.status_code == 200
    # Ürün linklerini kontrol et
    links = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    for link in links:
        href = link.get_attribute('href')
        if href:
            resp = requests.get(href)
            assert resp.status_code == 200 or resp.status_code == 302 
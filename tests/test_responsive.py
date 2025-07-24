import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

sizes = [
    (375, 667),   # iPhone 8
    (768, 1024),  # iPad
    (1440, 900),  # Desktop
]

@pytest.mark.parametrize("width,height", sizes)
def test_responsive_inventory(width, height):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(width, height)
    try:
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login('standard_user', 'secret_sauce')
        assert 'inventory' in driver.current_url
        products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        assert len(products) > 0
    finally:
        driver.quit() 
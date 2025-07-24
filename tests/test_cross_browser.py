import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

browsers = ["chrome", "firefox"]

@pytest.mark.parametrize("browser_name", browsers)
def test_login_inventory_cross_browser(browser_name):
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        try:
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            driver = webdriver.Firefox(options=options)
        except Exception:
            pytest.skip("Firefox veya geckodriver yüklü değil, test atlandı.")
            return
    else:
        pytest.skip(f"{browser_name} için destek yok.")
        return
    try:
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login('standard_user', 'secret_sauce')
        assert 'inventory' in driver.current_url
        # Ürün listesinin göründüğünü kontrol et
        products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        assert len(products) > 0
    finally:
        driver.quit() 
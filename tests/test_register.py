# Not: Bu test demo/örnek amaçlıdır, gerçek ortamda çalışmayabilir.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_register_example(driver):
    driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
    # E-posta gir ve hesap oluştur
    email = f'testuser{int(time.time())}@mail.com'
    driver.find_element(By.ID, 'email_create').send_keys(email)
    driver.find_element(By.ID, 'SubmitCreate').click()
    # Kayıt formunun yüklendiğini kontrol et
    driver.implicitly_wait(10)
    assert 'account-creation' in driver.current_url 
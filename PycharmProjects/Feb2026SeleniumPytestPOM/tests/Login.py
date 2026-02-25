import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_login:
    def test_login(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        time.sleep(4)
        # enter username
        name = driver.find_element(By.NAME, "username")
        name.send_keys("Admin")

        # enter password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")

        time.sleep(4)
        # click on login button

        Login = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        Login.click()

        assert "OrangeHRM" in driver.title







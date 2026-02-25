import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_MultiSelectRadio:
    def test_multiradio(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # enter username
        name = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        name.send_keys("Admin")

        # enter password
        password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password.send_keys("admin123")

        time.sleep(4)
        # click on login button

        Login = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        Login.click()

        assert "OrangeHRM" in driver.title

        pim = driver.find_element(By.LINK_TEXT, "PIM")
        pim.click()

        time.sleep(3)
        # click on check box one by one
        checkbox_list = driver.find_elements(By.XPATH, "//i[@class = 'oxd-icon bi-check oxd-checkbox-input-icon']")
        count = len(checkbox_list)
        print(count)

        # Iterate the list
        for i in range(1, checkbox_list):
            time.sleep(2)
            i.click()

        # close only the  current browser session
        driver.close()









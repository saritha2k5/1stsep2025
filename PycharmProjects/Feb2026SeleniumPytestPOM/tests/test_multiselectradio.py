import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_MultiSelectRadio:

    def test_multiradio(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        # click on check box one by one
        checkbox_list = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
        count = len(checkbox_list)
        print(count)

        # Iterate the list
        for i in checkbox_list:
            time.sleep(2)
            i.click()

        # close only the current browser session
        driver.close()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_radio:
    def test_radio(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        time.sleep(2)

        radio = driver.find_element(By.XPATH, "//input[@value='radio1']")
        radio.click()

        assert radio.is_selected()

        driver.quit()
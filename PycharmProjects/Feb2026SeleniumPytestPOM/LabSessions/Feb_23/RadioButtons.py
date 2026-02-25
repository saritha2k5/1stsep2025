import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Radio_Checkbox:

    def test_radio_checkbox(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://testautomationpractice.blogspot.com/")

        time.sleep(3)

        # -------- Select Gender Radio Button --------
        male_radio = driver.find_element(By.ID, "male")
        male_radio.click()

        # Verify Male is selected
        assert male_radio.is_selected()

        time.sleep(2)

        # -------- Select Days Checkboxes --------
        monday_checkbox = driver.find_element(By.ID, "monday")
        sunday_checkbox = driver.find_element(By.ID, "sunday")

        monday_checkbox.click()
        sunday_checkbox.click()

        # Verify Checkboxes are selected
        assert monday_checkbox.is_selected()
        assert sunday_checkbox.is_selected()

        time.sleep(3)

        driver.quit()
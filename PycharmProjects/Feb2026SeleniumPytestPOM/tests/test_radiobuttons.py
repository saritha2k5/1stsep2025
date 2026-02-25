import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_radio_button:

    def test_radio_buttons(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        time.sleep(2)

        # click radio1
        driver.find_element(By.XPATH, "//input[@value='radio1']").click()
        time.sleep(1)

        # click radio2
        driver.find_element(By.XPATH, "//input[@value='radio2']").click()

        # assertion
        assert driver.find_element(
            By.XPATH, "//input[@value='radio2']"
        ).is_selected()

        driver.quit()
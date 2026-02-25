from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


class Test_Radio:

    def test_radio(self):

        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )

        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        time.sleep(4)

        # ---------------------------
        # Simple Alert
        # ---------------------------
        simplealt = driver.find_element(
            By.XPATH, "//button[normalize-space()='Click for JS Alert']"
        )
        simplealt.click()

        alt = driver.switch_to.alert
        alt.accept()   # Click OK


        # ---------------------------
        # Confirmation Alert
        # ---------------------------
        confalt = driver.find_element(
            By.XPATH, "//button[normalize-space()='Click for JS Confirm']"
        )
        confalt.click()

        alt = driver.switch_to.alert
        alt.dismiss()   # Click Cancel


        # ---------------------------
        # Prompt Alert
        # ---------------------------
        promptalt = driver.find_element(
            By.XPATH, "//button[normalize-space()='Click for JS Prompt']"
        )
        promptalt.click()

        alt = driver.switch_to.alert
        alerttext = alt.text
        print(alerttext)

        alt.send_keys("test hello")
        alt.accept()

        time.sleep(2)
        driver.close()
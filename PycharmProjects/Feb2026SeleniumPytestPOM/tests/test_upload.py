from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_Upload:

    def test_up(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)

        # Locate file upload input
        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")
        browse.send_keys("C:/state1.txt")   # Update with your file path
        time.sleep(2)

        # Click upload button
        upload = driver.find_element(By.XPATH, "//input[@id='file-submit']")
        upload.click()
        time.sleep(2)

        # Verify upload success
        fileupload = driver.find_element(
            By.XPATH, "//h3[normalize-space()='File Uploaded!']"
        )

        assert fileupload.text == "File Uploaded!"

        time.sleep(2)
        driver.close()
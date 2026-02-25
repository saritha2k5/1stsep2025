import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

DOWNLOAD_DIR = r"C:\Users\vinod kumar\Downloads"

class Test_download:

    def test_dw(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        file_link = driver.find_element(By.XPATH, "//a[normalize-space()='alert.jpeg']")
        file_link.click()

        # Verify file downloaded
        file_path = os.path.join(DOWNLOAD_DIR, "alert.jpeg")
        time.sleep(3)  # wait for download

        assert os.path.exists(file_path)

        driver.quit()
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

        links = driver.find_elements(By.TAG_NAME, "a")
        count = len(links)
        print(count)

        for link in links:
            print(link.text)

        time.sleep(2)
        driver.close()
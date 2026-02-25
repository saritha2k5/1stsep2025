from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_Wind:

    def test_alerts(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.maximize_window()
        driver.implicitly_wait(10)

        clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
        clickhere.click()

        # fetch the window handles of both tabs
        windows = driver.window_handles
        print(windows)

        # move the control to the child window
        driver.switch_to.window(windows[1])

        text = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
        print(text.text)

        driver.close()

        # get back to parent window
        driver.switch_to.window(windows[0])
        print("Back to parent window")

        driver.quit()
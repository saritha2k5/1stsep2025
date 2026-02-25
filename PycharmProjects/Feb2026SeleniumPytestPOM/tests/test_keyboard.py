from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_Keyboard:

    def test_keyboard(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(2)

        actions = ActionChains(driver)

        # Locate username and password fields
        username = driver.find_element(By.XPATH, "//input[@name='email']")
        password = driver.find_element(By.XPATH, "//input[@name='pass']")

        # Type username
        username.send_keys("testuser123")
        time.sleep(1)

        # CTRL + A (Select All)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        time.sleep(1)

        # CTRL + C (Copy)
        actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        time.sleep(1)

        # Move to password field
        password.click()
        time.sleep(1)

        # CTRL + V (Paste)
        actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(2)

        driver.close()
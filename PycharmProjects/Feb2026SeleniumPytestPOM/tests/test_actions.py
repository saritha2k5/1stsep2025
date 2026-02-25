from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time


class Test_Actions:

    def test_actions(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.maximize_window()
        driver.get("https://www.amazon.in/")
        time.sleep(2)

        actions = ActionChains(driver)

        # Double Click
        bestsellers = driver.find_element(
            By.XPATH,
            "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']"
        )
        actions.double_click(bestsellers).perform()
        time.sleep(2)

        driver.back()
        time.sleep(2)

        # Right Click
        mobiles = driver.find_element(
            By.CSS_SELECTOR,
            ".nav-a[href='/mobile-phones/b/?ie=UTF8&node=1389401031']"
        )
        actions.context_click(mobiles).perform()
        time.sleep(2)

        driver.back()
        time.sleep(2)

        # Move to element
        primes = driver.find_element(
            By.XPATH,
            "//span[normalize-space()='Prime']"
        )
        actions.move_to_element(primes).perform()
        time.sleep(2)

        # Click and Hold
        fresh = driver.find_element(
            By.XPATH,
            "//span[normalize-space()='Fresh']"
        )
        actions.click_and_hold(fresh).perform()
        time.sleep(2)

        driver.close()
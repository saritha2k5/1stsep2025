from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

class Test_waits:

    def test_waits(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("https://www.facebook.com/")
        driver.maximize_window()

        # This is a global setting that applies to every element location call for the entire session
        driver.implicitly_wait(2)

        # explicit wait
        radio_btn = driver.find_element(By.XPATH, "(//input[@value='radio2'])[1]")
        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda _: radio_btn.is_displayed())

        # custom wait or fluent wait
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
        wait.until(lambda _: radio_btn.send_keys("Displayed") or True)

        driver.close()
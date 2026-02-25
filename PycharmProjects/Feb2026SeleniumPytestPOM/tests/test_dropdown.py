from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager
import time


class Test_DropDown:

    def test_dropdown(self):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )
        driver.maximize_window()

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(2)

        dropdown = driver.find_element(By.ID, "dropdown-class-example")

        # Select class is used for drop downs
        sel = Select(dropdown)

        # Select by visible text
        sel.select_by_visible_text("Option1")
        time.sleep(2)

        # Select by value
        sel.select_by_value("option2")
        time.sleep(2)

        # Select by index
        sel.select_by_index(3)
        time.sleep(2)

        driver.quit()
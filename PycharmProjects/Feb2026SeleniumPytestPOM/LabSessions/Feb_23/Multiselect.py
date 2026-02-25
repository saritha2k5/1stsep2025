from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Test_MultiSelect_Checkbox:

    def test_multiselect_and_checkbox(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.maximize_window()

        driver.get("https://trytestingthis.netlify.app/")

        wait = WebDriverWait(driver, 10)

        # ----------------------------
        # Multi Select Dropdown
        # ----------------------------
        multi_dropdown = wait.until(
            EC.presence_of_element_located((By.ID, "owc"))
        )

        select = Select(multi_dropdown)
        select.select_by_visible_text("Option 1")

        # ----------------------------
        # Choose applicable options (Checkboxes)
        # ----------------------------
        checkbox1 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox'][1]"))
        )

        checkbox2 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox'][2]"))
        )

        checkbox1.click()
        checkbox2.click()

        driver.quit()
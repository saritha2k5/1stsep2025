from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://trytestingthis.netlify.app/")
time.sleep(2)

dropdown = Select(driver.find_element(By.ID, "owc"))


dropdown.select_by_value("option 1")
dropdown.select_by_value("option 3")

time.sleep(2)


print("Selected Options:")
for option in dropdown.all_selected_options:
    print(option.text)


dropdown.deselect_all()
print("All options deselected")

time.sleep(2)
driver.quit()
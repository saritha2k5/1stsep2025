from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_webtable():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://the-internet.herokuapp.com/tables")

    print("Page Title:", driver.title)

    # Fetch number of rows
    rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
    print("Total Rows:", len(rows))

    for row in rows:
        print("Row Data:", row.text)

    time.sleep(2)

    # Fetch number of columns
    cols = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td")
    print("Total Columns:", len(cols))

    for col in cols:
        print("Column Data:", col.text)

    time.sleep(2)

    # Fetch specific cell data
    celldata = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[4]")
    print("Cell Data:", celldata.text)

    assert "$100.00" in celldata.text

    driver.quit()
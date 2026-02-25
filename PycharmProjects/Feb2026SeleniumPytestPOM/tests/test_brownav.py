import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# navigate to url
driver.get("https://trytestingthis.netlify.app/")
time.sleep(2)

# browser interactions
title = driver.title
print(title)

url = driver.current_url
print(url)

time.sleep(2)

# navigational commands
driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

driver.quit()
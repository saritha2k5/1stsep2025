from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


class Test_SwagLabs:

    def test_complete_order(self):

        driver = None

        try:
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install())
            )
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

            # -------------------------
            # Open Website
            # -------------------------
            driver.get("https://www.saucedemo.com/")

            # -------------------------
            # Login
            # -------------------------
            wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()

            # -------------------------
            # Add Item to Cart
            # -------------------------
            wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

            # -------------------------
            # Click Cart Icon
            # -------------------------
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

            # -------------------------
            # Click Checkout
            # -------------------------
            wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

            # -------------------------
            # Enter Information
            # -------------------------
            wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Vinod")
            driver.find_element(By.ID, "last-name").send_keys("Reddy")
            driver.find_element(By.ID, "postal-code").send_keys("520001")

            driver.find_element(By.ID, "continue").click()

            # -------------------------
            # Click Finish
            # -------------------------
            wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

            # -------------------------
            # Verify Thank You Message
            # -------------------------
            thank_you_text = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
            ).text

            assert "Thank you for your order!" in thank_you_text
            print("Order completed successfully ")

        except Exception as e:
            print("Test Failed ")
            print("Error:", e)

        finally:
            if driver:
                time.sleep(3)
                driver.quit()
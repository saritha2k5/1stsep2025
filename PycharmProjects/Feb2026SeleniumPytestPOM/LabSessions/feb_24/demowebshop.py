import pytest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestDemoWebShopFull:

    def test_complete_e2e(self):

        driver = None

        try:
            # ================= BROWSER SETUP =================
            chrome_options = Options()
            chrome_options.add_argument("--guest")

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)

            driver.maximize_window()
            driver.implicitly_wait(5)

            wait = WebDriverWait(driver, 15)

            # Generate unique email
            email = f"testuser{random.randint(1000,9999)}@mail.com"
            password = "Test@123"

            # ================= REGISTER =================
            driver.get("https://demowebshop.tricentis.com/")
            time.sleep(1)

            driver.find_element(By.LINK_TEXT, "Register").click()
            time.sleep(1)

            driver.find_element(By.ID, "gender-male").click()
            driver.find_element(By.ID, "FirstName").send_keys("Vinod")
            driver.find_element(By.ID, "LastName").send_keys("Tester")
            driver.find_element(By.ID, "Email").send_keys(email)
            driver.find_element(By.ID, "Password").send_keys(password)
            driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
            time.sleep(1)

            driver.find_element(By.ID, "register-button").click()
            time.sleep(2)

            assert "completed" in driver.page_source.lower()

            # Logout
            driver.find_element(By.LINK_TEXT, "Log out").click()
            time.sleep(1)

            # ================= LOGIN =================
            driver.find_element(By.LINK_TEXT, "Log in").click()
            time.sleep(1)

            driver.find_element(By.ID, "Email").send_keys(email)
            driver.find_element(By.ID, "Password").send_keys(password)
            time.sleep(1)

            driver.find_element(By.XPATH, "//input[@value='Log in']").click()
            time.sleep(2)

            assert "Log out" in driver.page_source

            # ================= ADD PRODUCT =================
            driver.find_element(By.LINK_TEXT, "Books").click()
            time.sleep(1)

            driver.find_element(By.XPATH, "//input[@value='Add to cart']").click()
            time.sleep(2)

            driver.find_element(By.LINK_TEXT, "Shopping cart").click()
            time.sleep(1)

            driver.find_element(By.ID, "termsofservice").click()
            time.sleep(1)

            driver.find_element(By.ID, "checkout").click()
            time.sleep(2)

            # ================= BILLING ADDRESS =================
            Select(wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )).select_by_visible_text("India")

            time.sleep(1)

            driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Hyderabad")
            driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Test Street 123")
            driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("500001")
            driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("9876543210")
            time.sleep(1)

            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@onclick='Billing.save()']"))
            ).click()
            time.sleep(2)

            # ================= SHIPPING ADDRESS =================
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@onclick='Shipping.save()']"))
            ).click()
            time.sleep(2)

            # ================= SHIPPING METHOD =================
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@onclick='ShippingMethod.save()']"))
            ).click()
            time.sleep(2)

            # ================= PAYMENT METHOD =================
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@onclick='PaymentMethod.save()']"))
            ).click()
            time.sleep(2)

            # ================= PAYMENT INFO =================
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@onclick='PaymentInfo.save()']"))
            ).click()
            time.sleep(2)

            # ================= CONFIRM ORDER =================
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@onclick='ConfirmOrder.save()']"))
            ).click()
            time.sleep(3)

            assert "successfully processed" in driver.page_source.lower()

        except Exception as e:
            print("E2E Test Failed:", e)
            assert False

        finally:
            if driver:
                driver.quit()
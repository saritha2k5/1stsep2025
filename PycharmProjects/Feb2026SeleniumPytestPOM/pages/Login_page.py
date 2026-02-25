# check the title of the web page

import pytest

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_title(self):
        print(self.driver.title)
        assert "OrangeHRM" in self.driver.title



from selenium.webdriver.common.by import By


class LoginPage:

    # locators
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[normalize-space()='Login']")
    dashboard_text = (By.XPATH, "//h6[normalize-space()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver

    # enter username
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # enter password
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # click on login button
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
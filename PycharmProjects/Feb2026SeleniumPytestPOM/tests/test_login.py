import pytest

from pages.Login_page import LoginPage
@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_valid_login(self,driver):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        lp=LoginPage(driver)
        lp.login_button("Admin", "admin123")

    
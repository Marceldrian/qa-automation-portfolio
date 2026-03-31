import pytest
from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("standard_user", "secret_sauce")
        assert "/inventory" in driver.current_url

    def test_invalid_password(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("standard_user", "wrong_password")
        assert page.is_error_displayed()
        assert "Username and password do not match" in page.get_error_message()

    def test_empty_username(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("", "secret_sauce")
        assert page.is_error_displayed()

    def test_empty_password(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("standard_user", "")
        assert page.is_error_displayed()

    def test_locked_user(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("locked_out_user", "secret_sauce")
        assert "locked out" in page.get_error_message().lower()
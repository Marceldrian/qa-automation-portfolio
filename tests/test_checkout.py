import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:

    def reach_checkout(self, driver):
        """Login → add item → go to cart → click checkout"""
        lp = LoginPage(driver)
        lp.open()
        lp.login("standard_user", "secret_sauce")
        inv = InventoryPage(driver)
        inv.add_first_item_to_cart()
        inv.go_to_cart()
        CartPage(driver).click_checkout()

    def test_checkout_step_one_loads(self, driver):
        self.reach_checkout(driver)
        assert "checkout-step-one" in driver.current_url

    def test_valid_checkout_reaches_step_two(self, driver):
        self.reach_checkout(driver)
        page = CheckoutPage(driver)
        page.fill_info("Marcel", "D", "12345")
        page.click_continue()
        assert page.is_on_step_two()

    def test_empty_first_name_shows_error(self, driver):
        self.reach_checkout(driver)
        page = CheckoutPage(driver)
        page.fill_info("", "D", "12345")
        page.click_continue()
        assert page.is_error_displayed()
        assert "First Name is required" in page.get_error_message()

    def test_complete_order_shows_success(self, driver):
        self.reach_checkout(driver)
        page = CheckoutPage(driver)
        page.complete_checkout("Marcel", "D", "12345")
        assert "Thank you" in page.get_success_header()

    def test_empty_postal_code_shows_error(self, driver):
        self.reach_checkout(driver)
        page = CheckoutPage(driver)
        page.fill_info("Marcel", "D", "")
        page.click_continue()
        assert page.is_error_displayed()
        assert "Postal Code is required" in page.get_error_message()
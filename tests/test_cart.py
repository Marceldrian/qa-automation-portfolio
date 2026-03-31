import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:

    def add_item_and_go_to_cart(self, driver):
        lp = LoginPage(driver)
        lp.open()
        lp.login("standard_user", "secret_sauce")
        inv = InventoryPage(driver)
        inv.add_first_item_to_cart()
        inv.go_to_cart()

    def test_item_appears_in_cart(self, driver):
        self.add_item_and_go_to_cart(driver)
        page = CartPage(driver)
        assert page.get_item_count() == 1

    def test_cart_item_name_not_empty(self, driver):
        self.add_item_and_go_to_cart(driver)
        page = CartPage(driver)
        names = page.get_item_names()
        assert len(names) > 0
        assert names[0].strip() != ""

    def test_remove_item_from_cart(self, driver):
        self.add_item_and_go_to_cart(driver)
        page = CartPage(driver)
        page.remove_first_item()
        assert page.get_item_count() == 0

    def test_checkout_button_is_visible(self, driver):
        self.add_item_and_go_to_cart(driver)
        page = CartPage(driver)
        assert page.is_checkout_button_visible()

    def test_cart_url_is_correct(self, driver):
        self.add_item_and_go_to_cart(driver)
        assert "cart" in driver.current_url
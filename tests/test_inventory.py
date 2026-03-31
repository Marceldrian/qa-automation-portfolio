import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:

    def login(self, driver):
        lp = LoginPage(driver)
        lp.open()
        lp.login("standard_user", "secret_sauce")

    def test_products_are_displayed(self, driver):
        self.login(driver)
        page = InventoryPage(driver)
        page.is_loaded()
        assert page.get_product_count() == 6

    def test_product_names_not_empty(self, driver):
        self.login(driver)
        page = InventoryPage(driver)
        names = page.get_product_names()
        assert len(names) > 0
        assert all(name.strip() != "" for name in names)

    def test_sort_z_to_a(self, driver):
        self.login(driver)
        page = InventoryPage(driver)
        page.sort_by("za")
        names = page.get_product_names()
        assert names == sorted(names, reverse=True)

    def test_add_to_cart_updates_badge(self, driver):
        self.login(driver)
        page = InventoryPage(driver)
        assert page.get_cart_count() == 0
        page.add_first_item_to_cart()
        assert page.get_cart_count() == 1

    def test_navigate_to_cart(self, driver):
        self.login(driver)
        page = InventoryPage(driver)
        page.go_to_cart()
        assert "cart" in driver.current_url
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    PRODUCT_LIST      = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES     = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BTN   = (By.XPATH, "(//button[text()='Add to cart'])[1]")
    CART_BADGE        = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN     = (By.CLASS_NAME, "product_sort_container")
    CART_ICON         = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        return self.wait.until(
            EC.presence_of_element_located(self.PRODUCT_LIST)
        )

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_LIST))

    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in elements]

    def add_first_item_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def sort_by(self, option):
        dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        dropdown.select_by_value(option)

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
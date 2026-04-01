from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    PRODUCT_LIST  = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_BTN       = (By.XPATH, "(//button[text()='Add to cart'])[1]")
    CART_BADGE    = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_ICON     = (By.CLASS_NAME, "shopping_cart_link")
    CART_LIST     = (By.CLASS_NAME, "cart_list")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.presence_of_element_located(self.PRODUCT_LIST))

    def get_product_count(self):
        self.is_loaded()
        return len(self.driver.find_elements(*self.PRODUCT_LIST))

    def get_product_names(self):
        self.is_loaded()
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_NAMES)]

    def add_first_item_to_cart(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_BTN))
        btn.click()
        self.wait.until(EC.presence_of_element_located(self.CART_BADGE))

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def sort_by(self, option):
        Select(self.driver.find_element(*self.SORT_DROPDOWN)).select_by_value(option)

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()
        self.wait.until(EC.presence_of_element_located(self.CART_LIST))
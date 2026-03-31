from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    URL = "https://www.saucedemo.com/cart.html"

    # Locators
    CART_ITEMS        = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES        = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BTN        = (By.XPATH, "(//button[text()='Remove'])[1]")
    CHECKOUT_BTN      = (By.ID, "checkout")
    CONTINUE_BTN      = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        return "cart" in self.driver.current_url

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_item_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [el.text for el in elements]

    def remove_first_item(self):
        self.driver.find_element(*self.REMOVE_BTN).click()

    def is_checkout_button_visible(self):
        return self.driver.find_element(*self.CHECKOUT_BTN).is_displayed()

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()

    def click_continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()
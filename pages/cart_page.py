from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART_LIST    = (By.CLASS_NAME, "cart_list")
    CART_ITEMS   = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES   = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BTN   = (By.XPATH, "(//button[text()='Remove'])[1]")
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_BTN = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.presence_of_element_located(self.CART_LIST))

    def get_item_count(self):
        self.is_loaded()
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_item_names(self):
        self.is_loaded()
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]

    def remove_first_item(self):
        self.is_loaded()
        btn = self.wait.until(EC.element_to_be_clickable(self.REMOVE_BTN))
        btn.click()
        self.wait.until(EC.staleness_of(btn))

    def is_checkout_button_visible(self):
        self.is_loaded()
        btn = self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_BTN))
        return btn.is_displayed()

    def click_checkout(self):
        self.is_loaded()
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))

    def click_continue_shopping(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()
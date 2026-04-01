from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME     = (By.ID, "first-name")
    LAST_NAME      = (By.ID, "last-name")
    POSTAL_CODE    = (By.ID, "postal-code")
    CONTINUE_BTN   = (By.ID, "continue")
    ERROR_MSG      = (By.CSS_SELECTOR, "[data-test='error']")
    FINISH_BTN     = (By.ID, "finish")
    SUCCESS_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_info(self, first, last, postal):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        f = self.driver.find_element(*self.FIRST_NAME)
        f.clear()
        f.send_keys(first)
        l = self.driver.find_element(*self.LAST_NAME)
        l.clear()
        l.send_keys(last)
        p = self.driver.find_element(*self.POSTAL_CODE)
        p.clear()
        p.send_keys(postal)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def is_error_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG))
            return True
        except Exception:
            return False

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MSG)
        ).text

    def get_success_header(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_HEADER)
        ).text

    def is_on_step_two(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.FINISH_BTN))
            return True
        except Exception:
            return False

    def complete_checkout(self, first, last, postal):
        self.fill_info(first, last, postal)
        self.click_continue()
        self.click_finish()
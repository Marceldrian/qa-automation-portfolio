from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON   = (By.ID, "login-button")
    ERROR_MESSAGE  = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT))
        field.clear()
        field.send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def is_error_displayed(self):
        return len(self.driver.find_elements(*self.ERROR_MESSAGE)) > 0
import pytest
from utils.driver_factory import get_driver


@pytest.fixture(scope="function")
def driver():
    """Creates a fresh browser for each test, closes it after"""
    driver = get_driver()
    yield driver
    driver.quit()
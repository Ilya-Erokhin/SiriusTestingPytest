import pytest
from selenium import webdriver
from utilities.settings import BROWSER, BASE_URL
from pages.registration_page import RegistrationPage

@pytest.fixture(scope="function")
def driver():
    if BROWSER == "chrome":
        driver = webdriver.Chrome()
    elif BROWSER == "firefox":
        driver = webdriver.Firefox()
    elif BROWSER == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def open_url():
    return BASE_URL

@pytest.fixture(scope="function")
def registration_page(driver):
    page = RegistrationPage(driver)
    page.open_url()
    return page
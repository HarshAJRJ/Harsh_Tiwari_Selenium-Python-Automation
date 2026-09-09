from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from utilities.csv_reader import CSVReader
from utilities.config_reader import ConfigReader


def test_valid_login(driver):

    # Read test data from CSV
    test_data = CSVReader.read_data("testdata.csv")[0]

    email = test_data["email"]
    password = test_data["password"]

    # Read login URL from configuration
    config = ConfigReader()
    login_url = config.get("application", "login_url")

    # Open login page
    driver.get(login_url)

    # Create Login Page object
    login_page = LoginPage(driver)

    # Perform login
    login_page.login(email, password)

    # Wait for successful login navigation
    WebDriverWait(driver, 10).until(
        EC.url_contains("account/account")
    )

    # Verify successful login
    assert "account/account" in driver.current_url
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(
        "https://rahulshettyacademy.com/AutomationPractice/"
    )

    yield driver

    driver.quit()


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "smoke: marks tests as smoke tests"
    )

    config.addinivalue_line(
        "markers",
        "regression: marks tests as regression tests"
    )
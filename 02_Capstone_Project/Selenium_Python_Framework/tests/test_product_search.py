from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from utilities.config_reader import ConfigReader

def test_product_search(driver):

    # Open home page
    config = ConfigReader()
    url = config.get("application", "url")
    driver.get(url)

    # Create Home Page object
    home_page = HomePage(driver)

    # Search for product
    home_page.search_product("iphone")

    # Wait for search results page
    WebDriverWait(driver, 10).until(
        EC.url_contains("route=product/search")
    )

    # Get search result heading
    heading = home_page.get_search_result_heading()

    # Verify searched product appears in heading
    assert "iphone" in heading.lower()

    # Temporary failure for testing screenshot
    #assert False
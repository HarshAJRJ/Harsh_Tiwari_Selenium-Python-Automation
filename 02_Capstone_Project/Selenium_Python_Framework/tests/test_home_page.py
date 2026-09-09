from utilities.config_reader import ConfigReader


def test_home_page(driver):

    config = ConfigReader()

    url = config.get("application", "url")

    driver.get(url)

    assert "Your Store" in driver.title
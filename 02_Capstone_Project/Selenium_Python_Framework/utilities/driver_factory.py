from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from utilities.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver():

        config = ConfigReader()
        browser = config.get("application", "browser").lower()

        if browser == "chrome":

            driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                )
            )

            driver.maximize_window()
            return driver

        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
if __name__ == "__main__":

    driver = DriverFactory.get_driver()

    driver.get("https://tutorialsninja.com/demo/")

    input("Press Enter to close the browser...")

    driver.quit()
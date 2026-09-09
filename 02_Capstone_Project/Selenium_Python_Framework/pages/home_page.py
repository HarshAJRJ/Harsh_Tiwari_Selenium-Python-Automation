from selenium.webdriver.common.by import By


class HomePage:

    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    SEARCH_RESULT_HEADING = (By.CSS_SELECTOR, "#content h1")

    def __init__(self, driver):
        self.driver = driver

    def enter_search(self, product):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(product)

    def click_search(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def search_product(self, product):
        self.enter_search(product)
        self.click_search()

    def get_search_result_heading(self):
        return self.driver.find_element(
            *self.SEARCH_RESULT_HEADING
        ).text
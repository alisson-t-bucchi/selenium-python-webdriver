import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        return self.find_element(locator).click()

    def navbar_title(self, locator):
        assert self.find_element(locator).is_displayed(), f"Element {'locator'} not found!"

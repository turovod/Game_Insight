from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitMethods:
    def __init__(self, app):
        self.app = app

    def wait_for_element_present(self, by, error_message, timeout_in_seconds=10):
        wait = WebDriverWait(self.app.driver, timeout_in_seconds)
        return wait.until(expected_conditions.element_to_be_clickable(by), error_message)

    def wait_for_element_and_click(self, by, error_message, timeout_in_seconds=10):
        web_element = self.wait_for_element_present(by, error_message, timeout_in_seconds)
        web_element.click()
        return web_element

    def wait_for_element_and_sand_keys(self, by, error_message, keys, timeout_in_seconds=10):
        web_element = self.wait_for_element_present(by, error_message, timeout_in_seconds)
        web_element.send_keys(keys)
        return web_element


from selenium.common.exceptions import NoSuchElementException


class ServiceMethods:
    def __init__(self, app):
        self.driver = app.driver

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

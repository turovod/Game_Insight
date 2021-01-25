class NavigationHelper:
    def __init__(self, app):
        self.driver = app.driver

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

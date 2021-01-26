class NavigationMethods:
    def __init__(self, app):
        self.driver = app.driver
        self.base_url = app.base_url

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

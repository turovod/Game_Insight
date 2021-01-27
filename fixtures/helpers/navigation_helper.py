from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavigationMethods:
    def __init__(self, app):
        self.driver = app.driver
        self.base_url = app.base_url

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

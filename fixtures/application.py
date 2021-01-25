from selenium import webdriver
from fixtures import service_helper, navigation_helper


class Application:
    def __init__(self, browser, base_url):

        if browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=self.adapted_url_to_webdriver("drivers\geckodriver.exe"))
        elif browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=self.adapted_url_to_webdriver("drivers\chromedriver.exe"))
        elif browser == "edge":
            self.driver = webdriver.Edge(executable_path=self.adapted_url_to_webdriver("drivers\msedgedriver.exe"))
        else:
            raise ValueError(f"Unrecognised browser {browser}")
        self.base_url = base_url
        self.service_helper = service_helper
        self.navigation_helper = navigation_helper


    def adapted_url_to_webdriver(self, local_driver_url):
        wd_url = __file__
        wd_url = wd_url.strip("fixture\\application.py")
        wd_url = "\\".join([wd_url, local_driver_url])
        return wd_url

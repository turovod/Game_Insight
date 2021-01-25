from selenium import webdriver

from fixtures.get_file_url_helper import GetFileUrl
from fixtures.service_helper import ServiceMethods
from fixtures.navigation_helper import NavigationMethods


class Application:
    def __init__(self, browser, base_url):

        self.get_file_urls = GetFileUrl()

        if browser == "firefox":
            self.driver = webdriver.Firefox(
                executable_path=self.get_file_urls.get_file_url("sight\drivers\geckodriver.exe"))
        elif browser == "chrome":
            self.driver = webdriver.Chrome(
                executable_path=self.get_file_urls.get_file_url("sight\drivers\chromedriver.exe"))
        elif browser == "edge":
            self.driver = webdriver.Edge(
                executable_path=self.get_file_urls.get_file_url("sight\drivers\msedgedriver.exe"))
        else:
            raise ValueError(f"Unrecognised browser {browser}")

        self.base_url = base_url
        self.service_methods = ServiceMethods(self)
        self.navigation_methods = NavigationMethods(self)




from selenium import webdriver

from fixtures.get_file_url_helper import GetFileUrl
from fixtures.service_helper import ServiceMethods
from fixtures.navigation_helper import NavigationMethods
from model.session_model import SessionModel


class Application:
    def __init__(self, session_data):

        self.get_file_urls = GetFileUrl()

        if session_data['browser'] == "firefox":
            self.driver = webdriver.Firefox(
                executable_path=self.get_file_urls.get_file_url("sight\drivers\geckodriver.exe"))
        elif session_data['browser'] == "chrome":
            self.driver = webdriver.Chrome(
                executable_path=self.get_file_urls.get_file_url("sight\drivers\chromedriver.exe"))
        elif session_data['browser'] == "edge":
            self.driver = webdriver.Edge(
                executable_path=self.get_file_urls.get_file_url("sight\drivers\msedgedriver.exe"))
        else:
            raise ValueError(f"Unrecognised browser {session_data['browser']}")

        self.base_url = session_data['base_url']
        self.service_methods = ServiceMethods(self)
        self.navigation_methods = NavigationMethods(self)
        self.session_models = SessionModel(self, session_data)




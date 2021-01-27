from selenium import webdriver

from fixtures.helpers.get_file_url_helper import GetFileUrl
from fixtures.helpers.service_helper import ServiceMethods
from fixtures.helpers.navigation_helper import NavigationMethods
from fixtures.helpers.sett_localization_helper import SetLocalization
from fixtures.helpers.wait_helper import WaitMethods
from fixtures.tests_helpers.get_items_from_main_page_helper import ItemsFromMainPage
from fixtures.tests_helpers.get_projects_from_main_page_helper import ProjectListFromMainPage
from fixtures.tests_helpers.present_games_helper import PresentGame
from fixtures.tests_helpers.show_description_games_helper import ShowDescriptionGames
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
        self.localization = SetLocalization(self)
        self.wait_methods = WaitMethods(self)
        self.project_list_from_main_page = ProjectListFromMainPage(self)
        self.items_from_main_page = ItemsFromMainPage(self)
        self.present_games = PresentGame(self)
        self.show_descriptions_games = ShowDescriptionGames(self)













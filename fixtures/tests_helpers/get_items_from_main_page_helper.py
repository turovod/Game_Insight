from selenium.webdriver.common.by import By


class ItemsFromMainPage:
    def __init__(self, app):
        self.app = app

    def get_item_from_main_page(self):
        list_games_from_maine_page = self.app.project_list_from_main_page.get_project_list()
        slogan_text = self.app.wait_methods.wait_for_element_present((By.CLASS_NAME, "slogan"), "Slogan not present").text
        list_games_from_maine_page.append(slogan_text)

        return list_games_from_maine_page



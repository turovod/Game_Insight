
class ProjectListFromMainPage:
    def __init__(self, app):
        self.app = app

    def get_project_list(self):
        list_games_from_maine_page = []
        self.app.navigation_methods.open_home_page()
        self.app.localization.set_localization("en")
        list_web_elements = self.app.driver.find_elements_by_xpath("//div[@class='plate__title']")

        for element in list_web_elements:
            list_games_from_maine_page.append(element.text)

        return list_games_from_maine_page


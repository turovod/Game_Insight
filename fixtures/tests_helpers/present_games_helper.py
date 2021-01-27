from selenium.webdriver.common.by import By


class PresentGame:
    def __init__(self, app):
        self.app = app

    def get_name_present_game(self, by, game_name):
        self.app.navigation_methods.open_home_page()
        self.app.localization.set_localization("en")
        self.app.driver.find_element_by_class_name("plate__title").click()
        game_name = self.app.wait_methods.wait_for_element_present(by,
                                                                   f"Game {game_name} is not present").text

        return game_name

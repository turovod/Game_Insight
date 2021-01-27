from selenium.webdriver.common.by import By


class ShowDescriptionGames:
    def __init__(self, app):
        self.driver = app.driver
        self.app = app

    def show_description_game(self, by_game, tuple_by_wait, descripion_game_json):
        driver = self.driver
        self.app.navigation_methods.open_home_page()
        self.app.localization.set_localization("en")
        driver.find_element_by_css_selector(by_game).click()
        driver.set_window_size(300, 1000)
        self.app.wait_methods.wait_for_element_present(tuple_by_wait, "More is not aviable")
        self.app.wait_methods.wait_for_element_present((
            By.XPATH,
            "//*[contains(text(), '" + descripion_game_json + "')]"),
            "More is not aviable"
        )
        return True

        # print("--------------------")
        # print(app.session_models.session_model["en_description_airport_city"])
from selenium.webdriver.common.by import By


class SetLocalization:
    def __init__(self, app):
        self.app = app

    def set_localization(self, language):
        current_language = self.app.driver.find_element_by_xpath("//div[3]/div[2]/div/a").text
        if language != current_language:
            self.app.driver.find_element_by_xpath("//div[3]/div[2]/div/a").click()

            if language == "ru":
                self.app.wait_methods.wait_for_element_and_click((By.ID, "rus"), "Can't switch to Russian localization")
            if language == "en":
                self.app.wait_methods.wait_for_element_and_click((By.ID, "eng"), "Can't switch to English localization")
            if language == "lt":
                self.app.wait_methods.wait_for_element_and_click((By.ID, "lit"), "Can't switch to Lithuanian localization")




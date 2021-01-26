class SetLocalization:
    def __init__(self, app):
        self.app = app

    def set_localization(self, lang):
        target_lang = "eng"
        lang1 = "rus"
        lang2 = "lit"

        if lang == "lit":
            target_lang = "lit"
            lang2 = "eng"
        elif lang == "rus":
            target_lang = "rus"
            lang1 = "eng"

        try:
            self.app.driver.find_element_by_id(target_lang).click()
        except:
            try:
                self.app.driver.find_element_by_id(lang1).click()
                self.app.driver.find_element_by_id(target_lang).click()
            except:
                self.app.driver.find_element_by_id(lang2).click()
                self.app.driver.find_element_by_id(target_lang).click()






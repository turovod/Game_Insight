from selenium.webdriver.common.by import By


def test_section_the_tribes_is_present(app):
    list_games_from_json = app.session_models.session_model["en_games_list"]
    game_name = app.present_games.get_name_present_game((By.XPATH, "//li[2]/a/div"), list_games_from_json[1])

    assert game_name == list_games_from_json[1]


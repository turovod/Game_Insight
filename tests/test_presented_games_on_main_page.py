
def test_presented_games_on_main_page(app):
    list_games_from_json = app.session_models.session_model["en_games_list"]
    list_games_from_maine_page = app.project_list_from_main_page.get_project_list()

    assert sorted(list_games_from_maine_page) == sorted(list_games_from_json), "Projects on the main page do not match the games_list"


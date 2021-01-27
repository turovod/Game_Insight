import copy


def test_russian_localization(app):
    list_localized_data_from_json = copy.deepcopy(app.session_models.session_model["en_games_list"])
    list_localized_data_from_json.append(app.session_models.session_model["en_localized_data"])
    list_localized_items_from_main_page = app.items_from_main_page.get_item_from_main_page()

    assert sorted(list_localized_items_from_main_page) == sorted(list_localized_data_from_json), "English localization error"


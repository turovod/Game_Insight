
def test_presented_games_on_main_page(app):
    list_games_from_maine_page = []
    list_games_from_json = app.session_models.session_model["games_list"]

    app.navigation_methods.open_home_page()
    list_web_elements = app.driver.find_elements_by_xpath("//div[@class='plate__title']")

    for element in list_web_elements:
        list_games_from_maine_page.append(element.text)

    assert sorted(list_games_from_maine_page) == sorted(list_games_from_json)


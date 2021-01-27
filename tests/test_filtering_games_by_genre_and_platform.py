from selenium.webdriver.common.by import By


def test_filtering_games_by_genre_and_platform(app):
    description_airport_city = app.session_models.session_model["en_description_airport_city"]

    app.show_descriptions_games.show_description_game(
        "div.plate__title",
        (By.XPATH, "//div[@class='readmore__link_btn']"),
        description_airport_city
    )

    assert app.service_methods.is_element_present(
        "//*[contains(text(), "
        "'"+description_airport_city+"')]"
    ), f"Description {description_airport_city} not found"






import pytest
from fixtures.application import Application


fixture = None


@pytest.fixture
def app():
    global fixture

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_date['baseUrl'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture

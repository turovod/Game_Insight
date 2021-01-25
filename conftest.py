import os
import pytest
from fixtures.application import Application
import json


fixture = None


@pytest.fixture
def app():
    global fixture

    if fixture is None or not fixture.is_valid():
        url_session_data = "\\".join([os.path.dirname(__file__), "test_data\\session_data.json"])
        with open(url_session_data) as f:
            session_data = json.load(f)
        fixture = Application(browser=session_data["browser"], base_url=session_data["base_url"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.service_methods.destroy()

    request.addfinalizer(fin)
    return fixture

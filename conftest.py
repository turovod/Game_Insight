import os
import pytest
from fixtures.application import Application
import json


fixture = None


@pytest.fixture
def app():
    global fixture

    if fixture is None or not fixture.is_valid():
        url_session = "\\".join([os.path.dirname(__file__), "test_data\\session_data.json"])
        with open(url_session, encoding='utf-8') as f:
            session_data = json.load(f)
        fixture = Application(session_data=session_data)

    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.service_methods.destroy()

    request.addfinalizer(fin)
    return fixture

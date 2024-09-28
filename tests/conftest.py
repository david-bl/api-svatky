import pytest

from app import app as test_app
from app.config import TestConfig as Config


@pytest.fixture()
def app():
    app = test_app
    app.config.from_object(Config)

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

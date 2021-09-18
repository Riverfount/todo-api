import pytest
from mongoengine import connect, disconnect
from starlette.testclient import TestClient

from api.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def mongo(scope='function'):
    disconnect('default')
    db = connect('test_db', host='mongodb://localhost')
    yield db
    db.drop('test_db')
    disconnect('default')

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
    db.drop_database('test_db')
    disconnect('default')


@pytest.fixture
def users_data():
    return [
        {
            'name': 'Jorge Plautz',
            'password': '1234567890',
            'email': 'jplautz@example.com',
            'user_todo': [
                {
                    'id': '6158675285c8a31729632ab1',
                    'name': 'Estudar fastAPI'
                },
                {
                    'id': '6158675285c8a31729632ab2',
                    'name': 'Estudar MongoDB'
                },
            ]
        },
        {
            'name': 'Vicente Marçal',
            'password': '0987654321',
            'email': 'vmarcal@example.com',
            'user_todo': [
                {
                    'id': '6158675285c8a31729632bc1',
                    'name': 'Estudar fastAPI com Pydantic'
                },
                {
                    'id': '6158675285c8a31729632bc2',
                    'name': 'Estudar MongoDB com MongoEngine'
                },
            ]
        },
    ]

import pytest
from bson import ObjectId
from starlette import status


@pytest.fixture
def payload():
    return {
        'name': 'Jorge Plautz',
        'password': '1234567890',
        'email': 'jplautz@example.com'
    }


def test_insert_new_user_status_code_201_created(mongo, client, payload):
    response = client.post('/api/v1/users/', json=payload)
    assert response.status_code == status.HTTP_201_CREATED


def test_insert_new_user(mongo, client, payload):
    response = client.post('/api/v1/users/', json=payload)
    assert ObjectId.is_valid(response.json()['_id'])
    assert response.json()['name'] == 'Jorge Plautz'


@pytest.mark.parametrize(
    'payload', [
        {
            'password': '1234567890',
            'email': 'jplautz@example.com'
        },
        {
            'name': 'Jorge Plautz',
            'email': 'jplautz@example.com'
        },
        {
            'name': 'Jorge Plautz',
            'password': '1234567890',
        },
    ]
)
def test_insert_new_user_with_wrong_payload(mongo, client, payload):
    response = client.post('/api/v1/users/', json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

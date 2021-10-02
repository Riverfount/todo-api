from starlette import status

from api.users.data.users import UserData
from api.users.models.users import UserModelOut


def test_get_all_users_status_code_200_ok(client):
    response = client.get('/api/v1/users')
    assert response.status_code == status.HTTP_200_OK


def test_get_all_users_retrieve_all_users(mongo, client, users_data):
    for ud in users_data:
        ud_instance = UserData(**ud)
        ud_instance.save()
    response = client.get('/api/v1/users')
    expected = UserData.objects().as_pymongo().first()
    assert UserModelOut(**response.json()[0]) == UserModelOut(**expected)

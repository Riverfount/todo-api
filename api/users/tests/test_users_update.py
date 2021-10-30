from starlette import status

from api.users.data.users import UserData


def test_users_update_works_ok(mongo, client, users_data):
    for ud in users_data:
        ud_instance = UserData(**ud)
        ud_instance.save()
    user_id = UserData.objects(name='Vicente Marçal').scalar('id').first()
    user_update_data = {
        'password': 'x12W34@pQr'
    }
    response = client.patch(f'api/v1/users/{user_id}', json=user_update_data)
    user_updated = UserData.objects(id=user_id).scalar('password').first()
    assert response.status_code == status.HTTP_200_OK
    assert user_updated == user_update_data['password']

from datetime import datetime

from freezegun import freeze_time
from starlette import status

from api.users.data.users import UserData
from api.users.models.users import UserDetailModelOut


def test_get_user_detail_status_code_200_ok(mongo, client):
    user_id = '6158675285c8a31729632bc1'
    response = client.get(f'/api/v1/users/{user_id}')
    assert response.status_code == status.HTTP_200_OK


@freeze_time('2021-10-09T09:40:14')
def test_get_user_detail_works_ok(mongo, client, users_data):
    for ud in users_data:
        ud['created_at'] = datetime.now()
        UserData(**ud).save()
    user_id = UserData.objects.scalar('id').first()
    response = client.get(f'/api/v1/users/{user_id}')
    expected = UserData.objects(id=user_id).as_pymongo().first()

    assert UserDetailModelOut(**response.json()) == UserDetailModelOut(**expected)

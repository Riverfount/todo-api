from api.users.data.users import UserData
from api.users.models.users import UserModelOut


def get_all():
    users = UserData.objects().as_pymongo()
    users_list = [UserModelOut(**user) for user in users]
    return users_list

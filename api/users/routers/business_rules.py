from api.users.data.users import UserData
from api.users.models.users import UserAllModelOut, UserDetailModelOut
from api.utils.pydantic_oid import PyObjectId


def get_users(user_id: PyObjectId = None):
    if not user_id:
        users = UserData.objects().as_pymongo()
        users_response = [UserAllModelOut(**user) for user in users]
    else:
        user = UserData.objects(id=user_id).as_pymongo().first()
        users_response = UserDetailModelOut(**user) if user else None

    return users_response


def insert_user(user):
    new_user = UserData(**user.dict())
    new_user.save()
    return UserDetailModelOut(**new_user.to_mongo())

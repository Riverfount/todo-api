from typing import List

from fastapi import APIRouter

from api.users.models.users import UserAllModelOut, UserDetailModelOut, UserModelIn, UserUpdateModelIn
from api.users.routers.business_rules import get_users, insert_user, updater_user
from api.utils.pydantic_oid import PyObjectId

router = APIRouter(prefix='/api/v1/users', tags=['users'])


@router.get('/')
def get_all_users() -> List[UserAllModelOut]:
    return get_users()


@router.get('/{user_id}')
def get_user_detail(user_id: PyObjectId):
    return get_users(user_id)


@router.post('/', status_code=201)
def insert_new_user(user: UserModelIn) -> UserDetailModelOut:
    return insert_user(user)


@router.patch('/{user_id}')
def update_user(user_id: PyObjectId, user_update: UserUpdateModelIn):
    updater_user(user_id, user_update)

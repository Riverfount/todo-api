from typing import List

from fastapi import APIRouter

from api.users.models.users import UserAllModelOut
from api.users.routers.business_rules import get_users
from api.utils.pydantic_oid import PyObjectId

router = APIRouter(prefix='/api/v1/users', tags=['users'])


@router.get('/')
def get_all_users() -> List[UserAllModelOut]:
    return get_users()


@router.get('/{user_id}')
def get_user_detail(user_id: PyObjectId):
    return get_users(user_id)

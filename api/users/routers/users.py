from typing import List

from fastapi import APIRouter

from api.users.models.users import UserModelOut
from api.users.routers.business_rules import get_all

router = APIRouter(prefix='/api/v1/users', tags=['users'])


@router.get('/')
def get_all_users() -> List[UserModelOut]:
    return get_all()

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from api.utils.pydantic_oid import PyObjectId


class TodoGroupedModel(BaseModel):
    id: Optional[PyObjectId]
    name: str


class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(..., alias='_id')
    name: str
    created_at: Optional[datetime] = datetime.now().replace(microsecond=0)
    email: str
    password: str
    user_todo: List[Optional[TodoGroupedModel]]


class UserAllModelOut(BaseModel):
    id: Optional[PyObjectId] = Field(..., alias='_id')
    name: str


class UserDetailModelOut(BaseModel):
    id: Optional[PyObjectId] = Field(..., alias='_id')
    name: str
    created_at: Optional[datetime] = datetime.now().replace(microsecond=0)
    email: str
    user_todo: List[Optional[TodoGroupedModel]]


class UserModelIn(BaseModel):
    name: str
    password: str
    email: str
    user_todo: Optional[List[TodoGroupedModel]]

    class Config:
        schema_extra = {
            'example': {
                'name': 'Jorge Plautz',
                'password': '********',
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
            }
        }


class UserUpdateModelIn(BaseModel):
    name: Optional[str]
    password: Optional[str]
    email: Optional[str]
    user_todo: Optional[List[Optional[TodoGroupedModel]]]

    class Config:
        schema_extra = {
            'example': {
                'name': 'Jorge Plautz',
                'password': '********',
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
            }
        }

from typing import List
from enum import Enum
from pydantic import BaseModel


class TeamUser(BaseModel):
    id: int = 0
    name_team: str = ""


class TypeUser(int, Enum):
    ADMIN = 1
    USER = 2


class UserBase(BaseModel):
    login: str = ""
    type: TypeUser = 2
    name: str = ""
    sename: str = ""
    secondname: str = ""
    foto: str = "Photo/default.png"
    password: str = ""
    data: dict = {}


class UserGet(UserBase):
    id: int = 0

    class Config:
        orm_mode = True


class UserPost(UserBase):
    password: str = ""


class UserUpdate(UserBase):
    id: int = 0
    password: str = ""


class UserGetInTeam(BaseModel):
    id: int = 0
    name: str = ""
    sename: str = ""
    secondname: str = ""
    teams: List[TeamUser] = []


from pydantic import BaseModel
from datetime import datetime
from typing import List
from enum import Enum
from .Task import TaskGet


class TypeContest(int, Enum):
    OLIMPIADA = 1
    TEAM_OLIMPIADA = 2
    HACKATHON = 3


class TypeState(int, Enum):
    REGISTERED = 0
    CONFIRMED = 1
    GOING_ON = 2
    FINISHED = 3


class UserContest(BaseModel):
    id: int = 0
    sename: str = ""
    name: str = ""
    secondname: str = ""
    id_team: int = 0


class BaseContest(BaseModel):
    name_contest: str = ""
    datetime_start: datetime = datetime.now()
    datetime_end: datetime = datetime.now()
    datetime_registration: datetime = datetime.now()

    type: TypeContest = 1

    state_contest: TypeState = 0


class ContestGet(BaseContest):
    id: int = 0
    users: List[UserContest] = []
    tasks: List[TaskGet] = []

    class Config:
        orm_mode = True


class ContestPost(BaseContest):
    pass


class ContestDelete(BaseContest):
    id: int = 0


class ContestPutUsers(BaseModel):
    id: int = 0
    users: List[UserContest] = []


class ContestGetPage(BaseContest):
    id: int = 0
    tasks: List[TaskGet] = 0

    class Config:
        orm_mode = True


class ContestModelView(BaseContest):
    id: int
    name_contest: str
    type: TypeContest
    state_contest: TypeState
    data_start: str
    time_start: str
    data_end: str
    time_end: str

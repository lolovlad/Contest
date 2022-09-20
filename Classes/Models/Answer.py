from pydantic import BaseModel
from typing import List
from datetime import datetime


class UserAnswer(BaseModel):
    id: int
    name: str
    sename: str
    secondname: str


class TeamAnswer(BaseModel):
    id: int = 0
    name_team: str = ""


class TypeCompilationAnswer(BaseModel):
    id: int
    name_compilation: str


class BaseAnswer(BaseModel):
    date_send: datetime
    id_team: int = 0
    id_user: int
    id_task: int
    id_contest: int
    type_compiler: int
    total: str = "-"
    time: str = "-"
    memory_size: float
    number_test: int
    points: int


class AnswerGet(BaseAnswer):
    id: int

    user: UserAnswer
    team: TeamAnswer
    compilation: TypeCompilationAnswer

    class Config:
        orm_mode = True


class AnswerPost(BaseModel):
    id_user: int = 0
    id_contest: int = 0
    id_task: int = 0
    file: bytes = b""
    type_compilation: int = 1
    extension_file: str = ""


class Answers(BaseModel):
    menu: dict
    answers: List[AnswerGet]

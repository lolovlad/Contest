from pydantic import BaseModel
from typing import List
from enum import Enum
from ..Models.TaskView import TaskView


class TypeTask(int, Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    I = 5
    F = 6


class TypeInput(int, Enum):
    STREAM = 1
    FILE = 2


class TypeOutput(int, Enum):
    STREAM = 1
    FILE = 2


class BaseTask(BaseModel):
    id_contest: int = 0
    time_work: int = 1
    size_raw: int = 32
    type_input: TypeInput = 1
    type_output: TypeOutput = 1
    name_task: str = ""
    description: str = ""
    description_input: str = ""
    description_output: str = ""

    type_task: TypeTask = 1
    number_shipments: int = 100


class TaskGet(BaseTask):
    id: int = 0
    path_test_file: str = ""

    class Config:
        orm_mode = True


class TaskPost(BaseTask):
    file: bytes = b""


class TaskPut(BaseTask):
    id: int = 0
    file: bytes = b""
    path_test_file: str = ""


class TaskPostInServer(BaseTask):
    file: str = ""


class TaskPutInServer(BaseTask):
    id: int = 0
    file: str = ""
    path_test_file: str = ""


class TaskDelete(BaseTask):
    id: int = 0
    path_test_file: str = ""


class TaskPage(BaseTask):
    id: int = 0
    task_view: TaskView = None

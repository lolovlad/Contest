from pydantic import BaseModel
from enum import Enum


class TypeMessage(str, Enum):
    GET_SELECT_TASK = "get_select_task"
    GET_CONTEST = "get_contest"
    UPDATE_ANSWER = "update_answer"
    POTS_ANSWER = "post_answer"
    GET_LIST_TASK = "get_list_task"
    GET_LIST_ANSWER = "get_list_answer"
    GET_REPORT = "get_report"
    CLOSER_CONTEST = "close"


class User(BaseModel):
    token: str
    websocket: object


class BaseMessage(BaseModel):
    message: TypeMessage
    body_message: dict

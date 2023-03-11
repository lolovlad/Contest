from Classes.Models.WebSocketMessage import TypeMessage, BaseMessage
from settings import settings
from Classes.Session import Session

from json import loads

import eel


class ContestUserPage:
    def __init__(self, id_contest: int):
        self.__url_socket: str = f"ws://{settings.host_server}:{settings.port_server}/user_contest_view/view_contest?token={Session().token.access_token}"
        self.__id_contest: int = id_contest
        self.__id_task: int = 0
        self.__file_templates: dict = {
            "main": "templates/main_page.html",
        }

        self.__path_file_program: bytes = b""

    def show_view(self, **kwargs):
        eel.locationReplace(self.__file_templates["main"])

    def get_url_websocket(self):
        self.__url_socket = f"ws://{settings.host_server}:{settings.port_server}/user_contest_view/view_contest?token={Session().token.access_token}"
        return self.__url_socket

    def load_contest(self):
        return BaseMessage(message=TypeMessage.GET_CONTEST,
                           body_message={"id": self.__id_contest}).json()

    def load_main_window_list_task(self):
        return BaseMessage(message=TypeMessage.GET_LIST_TASK,
                           body_message={"id": self.__id_contest}).json()

    def load_main_window_select_task(self, id_task: int):
        return BaseMessage(message=TypeMessage.GET_SELECT_TASK,
                           body_message={"id": id_task}).json()

    def get_report(self, id_answer: int):
        return BaseMessage(message=TypeMessage.GET_REPORT,
                           body_message={"id_answer": id_answer}).json()

    def get_list_answers(self, id_task: int):
        return BaseMessage(message=TypeMessage.GET_LIST_ANSWER,
                           body_message={"id_task": id_task,
                                         "token": Session().token,
                                         "id_contest": self.__id_contest}).json()

    def set_file(self, file: dict):
        self.__path_file_program = open(file["file_name"], "rb").read().decode()

    def send_answer(self, id_task: int, id_compiler: int):
        return BaseMessage(message=TypeMessage.POTS_ANSWER,
                           body_message={"id_task": id_task,
                                         "token": Session().token,
                                         "id_contest": self.__id_contest,
                                         "id_compiler": id_compiler,
                                         "program_file": self.__path_file_program}).json()

    def close_contest(self):
        return BaseMessage(message=TypeMessage.CLOSER_CONTEST,
                           body_message={"token": Session().token,
                                         "id_contest": self.__id_contest}).json()

    def parser_message(self, message: str):
        message = loads(message)
        if message["message"] == TypeMessage.GET_CONTEST:
            eel.setContestInformation(message["body_message"])
        if message["message"] == TypeMessage.GET_LIST_TASK:
            eel.setTaskList(message["body_message"]["list_task"])
        if message["message"] == TypeMessage.GET_SELECT_TASK:
            eel.setSelectTask(message["body_message"])
        if message["message"] == TypeMessage.GET_LIST_ANSWER:
            eel.setAnswer(message["body_message"]["list"])
        if message["message"] == TypeMessage.GET_REPORT:
            eel.setReport(message["body_message"]["report"])
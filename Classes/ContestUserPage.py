from Classes.Models.WebSocketMessage import TypeMessage, BaseMessage
from settings import settings
from Classes.Session import Session
from Classes.ProxyController.UserContestViewProxy import UserContestViewProxy

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
        self.__proxy: UserContestViewProxy = UserContestViewProxy()
        self.__path_file_program: bytes = b""

    def show_view(self, **kwargs):
        eel.locationReplace(self.__file_templates["main"])

    def get_url_websocket(self):
        self.__url_socket = f"ws://{settings.host_server}:{settings.port_server}/user_contest_view/view_contest?token={Session().token.access_token}"
        return self.__url_socket

    def load_contest(self) -> dict:
        return self.__proxy.get_contest(self.__id_contest)["body_message"]

    def load_main_window_list_task(self) -> dict:
        return self.__proxy.get_list_task(self.__id_contest)["body_message"]["list_task"]

    def load_main_window_select_task(self, id_task: int) -> dict:
        return self.__proxy.get_task(id_task)["body_message"]

    def get_report(self, id_answer: int) -> dict:
        return self.__proxy.get_report(id_answer)["body_message"]["report"]

    def get_list_answers(self, id_task: int) -> dict:
        return self.__proxy.get_list_answers(self.__id_contest, id_task)["body_message"]["list"]

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
        self.__proxy.close_contest(self.__id_contest)

    def parser_message(self, message: str):
        message = loads(message)
        if message["message"] == TypeMessage.POTS_ANSWER:
            eel.getListAnswer()
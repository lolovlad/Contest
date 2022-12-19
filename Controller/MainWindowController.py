from typing import List
from Classes.Session import Session

from Classes.ProxyController.ContestProxy import ContestProxy
from Classes.ProxyController.UserProxy import UserProxy
from Classes.ProxyController.AnswersProxy import AnswersProxy

from Classes.ProxyController.MainProxy import MainProxy

from View.MainWindowView import MainWindowView
from Model.MainWindowModel import MainWindowModel
from Classes.Models import Menu
from json import dumps
from Interfase import Controller
from Classes.Models.Message import TypeStatus, StatusUser


class MainWindowController(Controller):
    def __init__(self, model: MainWindowModel = MainWindowModel()):
        self.__model = model
        self.__view: MainWindowView = MainWindowView(self, self.__model)
        self.__proxy_contest: ContestProxy = ContestProxy()
        self.__proxy_user: UserProxy = UserProxy()
        self.__proxy_answers: AnswersProxy = AnswersProxy()

        self.__proxy_main: MainProxy = MainProxy() # Удалить эту залупу сука

    def show_view(self, contest: Menu):
        self.__model.id_contest = contest.contests.id
        self.__view.show_view()

    def load_contest(self):
        response = self.__proxy_contest.contest_page(self.__model.id_contest)
        self.__model.contest = response

    def load_compilation(self) -> List[dict]:
        is_send, response = self.__proxy_main.load_to_database_compilation({})
        if is_send:
            return response
        return []

    def load_answer(self, data: dict):
        response = self.__proxy_answers.get_answers(self.__model.contest["id"], data["id_task"])
        self.__model.answers = response["answers"]
        self.__model.menu = response["menu"]

    def load_report(self, id_answer: int):
        response = self.__proxy_answers.get_report(id_answer)
        self.__model.select_report = response

    def select_task(self, id_task):
        self.__model.select_task = id_task

    def send_answer(self):
        self.__model.select_answer = {"id_contest": self.__model.contest["id"],
                                      "id_user": 0,
                                      "extension_file": self.__model.file["extension_file"]}
        data = self.__model.select_answer
        try:
            data["file"] = open(self.__model.file["file_name"], "rb").read().decode("utf-8")
        except Exception:
            pass

        response = self.__proxy_answers.post_answers(data)
        print(response)
        self.__model.add_answer(response)

    def close_contest(self):
        self.__proxy_contest.close_to_user_contest(self.__model.id_contest, 0)
        self.__view.update("close_contest")

    def is_close_contest(self):
        response = self.__proxy_user.get_status_user(self.__model.id_contest, 0)
        status = StatusUser(**response)
        return status.status != TypeStatus.GRANTED

    def open_package_window(self, controller):
        controller.show_view(self.__model.contest["id"])

    def set_select_answer(self, value: dict):
        self.__model.select_answer = value

    def set_file(self, value: dict):
        self.__model.file = value

from typing import List
from Classes.Session import Session
from Classes.ProxyController.MainProxy import MainProxy
from View.MainWindowView import MainWindowView
from Model.MainWindowModel import MainWindowModel
from Classes.Models import Menu
from json import dumps
from Interfase import Controller
from Classes.Models.Message import TypeStatus, StatusUser


class MainWindowController(Controller):
    def __init__(self, model: MainWindowModel = MainWindowModel(), proxy: MainProxy = MainProxy()):
        self.__model = model
        self.__view: MainWindowView = MainWindowView(self, self.__model)
        self.__proxy = proxy

    def show_view(self, contest: Menu):
        self.__model.id_contest = contest.contests.id
        self.__view.show_view()

    def load_contest(self):
        data = {"id_contest": self.__model.id_contest}
        is_send, response = self.__proxy.load_to_database_contest_page(data)
        if is_send:
            self.__model.contest = response

    def load_compilation(self) -> List[dict]:
        is_send, response = self.__proxy.load_to_database_compilation({})
        if is_send:
            return response
        return []

    def load_answer(self, data: dict):
        data["id_user"] = Session().user.id
        data["id_contest"] = self.__model.contest["id"]
        is_send, response = self.__proxy.load_to_database_answers(data)
        if is_send:
            self.__model.answers = response["answers"]
            self.__model.menu = response["menu"]

    def load_report(self, id_answer: int):
        data = {
            "id_answer": id_answer
        }
        is_send, response = self.__proxy.load_to_database_json_report(data)
        if is_send:
            self.__model.select_report = response

    def select_task(self, id_task):
        self.__model.select_task = id_task

    def send_answer(self):
        self.__model.select_answer = {"id_contest": self.__model.contest["id"],
                                      "id_user": Session().user.id,
                                      "extension_file": self.__model.file["extension_file"]}
        data = self.__model.select_answer
        try:
            data["file"] = open(self.__model.file["file_name"], "rb").read().decode("utf-8")
        except Exception:
            pass

        response = self.__proxy.add_answer(data)
        print(response)
        self.__model.add_answer(response)

    def close_contest(self):
        data = {
            "id_user": Session().user.id,
            "id_contest": self.__model.id_contest
        }
        self.__proxy.close_contest_to_user(data)
        self.__view.update("close_contest")

    def is_close_contest(self):
        data = {
            "id_user": Session().user.id,
            "id_contest": self.__model.id_contest
        }
        response = self.__proxy.get_status_user(data)
        status = StatusUser(**response)
        return status.status != TypeStatus.GRANTED

    def open_package_window(self, controller):
        controller.show_view(self.__model.contest["id"])

    def set_select_answer(self, value: dict):
        self.__model.select_answer = value

    def set_file(self, value: dict):
        self.__model.file = value

import requests
from Classes.Session import Session
from Classes.ProxyController.MainProxy import MainProxy
from View.PackageView import PackageView
from json import loads
import eel


class PackageController:
    def __init__(self, model):
        self.__model = model
        self.__view = PackageView(self, self.__model)
        self.__proxy = MainProxy()
        self.__model.attach(self.__view)

    def load_answer_package(self):
        data = {
            "id_task": 0,
            "id_team": Session().user.team.id,
            "id_contest": self.__model.id_contest
        }
        is_send, response = self.__proxy.load_to_database_answers(data)
        main = response[1]["answers"]
        self.__model.answers = main

    def load_report_package(self, id_report):
        data = {
            "id_report": id_report
        }
        is_send, response = self.__proxy.load_to_database_json_report(data)
        self.__model.select_report = loads(response[1])

    def show_view(self, id_contest):
        self.__model.id_contest = id_contest
        self.__view.show_view()
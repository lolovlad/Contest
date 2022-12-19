import requests
from Classes.Session import Session
from Classes.ProxyController.MainProxy import MainProxy
from Model.PackageModel import PackageModel
from View.PackageView import PackageView
from json import loads
import eel


class PackageController:
    def __init__(self, model: PackageModel = PackageModel()):
        self.__model = model
        self.__view: PackageView = PackageView(self, self.__model)
        self.__proxy: MainProxy = MainProxy()
        self.__model.attach(self.__view)

    def load_answer_package(self):
        data = {
            "id_user": Session().user.id,
            "id_contest": self.__model.id_contest
        }
        is_send, response = self.__proxy.load_to_database_package(data)
        if is_send:
            self.__model.answers = response

    def load_report_package(self, id_answer: int):
        data = {
            "id_answer": id_answer
        }
        is_send, response = self.__proxy.load_to_database_json_report(data)
        if is_send:
            self.__model.select_report = response

    def show_view(self, id_contest: int):
        self.__model.id_contest = id_contest
        self.__view.show_view()
import requests
from Classes.Session import Session
from Classes.ProxyController.MainProxy import MainProxy
from View.MainWindowView import MainWindowView
from json import dumps, loads
from pykson import Pykson
import eel


class MainWindowController:
    def __init__(self, model):
        self.__model = model
        self.__view = MainWindowView(self, self.__model)
        self.__proxy = MainProxy()

    def show_view(self, contest):
        self.__view.show_view(contest)

    def default(self):
        pass

    def load_contest(self):
        self.__model.notify("contests")

    def load_tasks_on_contest(self):
        data = {
            "list_name_file": dumps({"name_files": [task["path_test_file"] for task in self.__model.tasks]})
        }
        is_send, response = self.__proxy.load_to_database_json_test_file(data)

        json = response[1]["jsons_view"]

        self.__model.files = json

        self.__model.notify("tasks_update")

    def load_answer(self):
        data = {
            "id_task": 0,
            "id_team": Session().user.team.id,
            "id_contest": self.__model.contest["id"]
        }
        is_send, response = self.__proxy.load_to_database_answers(data)
        main = response[1]["answers"]

        menu = self.__model.menu
        select_answer = []
        if len(main) > 0:
            for id_task in self.__model.id_list_task():
                answer_task = list(sorted(main, key=lambda x: x["points"] and
                                                              x["task"]["id"] == id_task, reverse=True))[0]
                menu[id_task] = {"total": answer_task["total"],
                                 "points": answer_task["points"]}
                select_answer = list(filter(lambda x: x["task"]["id"] == self.__model.select_task["id"], main))
        self.__model.select_answers = select_answer
        self.__model.menu = menu

    def load_report(self, id_report):
        data = {
            "id_report": id_report
        }
        is_send, response = self.__proxy.load_to_database_json_report(data)
        self.__model.select_report = loads(response[1])

    def select_task(self, id_task):
        self.__model.select_task = id_task

    def send_answer(self):
        response = {
            "id_task": self.__model.select_task["id"]
        }

        data = {"id_team": Session().user.team.id,
                "id_user": Session().user.id,
                "extension_file": "py"}
        try:
            data["file"] = open(self.__model.file, "rb").read().decode("utf-8")
        except Exception:
            pass

        response["data"] = dumps(data)
        is_send, response = self.__proxy.add_answer(response)
        print(response)
        self.load_answer()

    def close_contest(self):
        Session().user.team.state_contest = 2
        json_team = Pykson().to_dict_or_list(Session().user.team)
        data = {
            "id_team": 1,
            "team": dumps(json_team)
        }
        is_send, response = self.__proxy.update_team(data)
        self.__view.update("close_contest")

    def is_close_contest(self):
        return Session().user.team.state_contest == 2

    def open_package_window(self, controller):
        controller.show_view(self.__model.contest["id"])

    def set_file(self, path_file):
        self.__model.file = path_file
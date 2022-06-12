import requests
from Classes.Session import Session
from View.TotalWindowView import TotalWindowView
from json import dumps, loads
from pykson import Pykson
from Classes.EelModification import EelModification
from Classes.ProxyController.AdminPanelAPI import AdminPanelAPI
import eel


class TotalWindowController:
    def __init__(self, model):
        self.__model = model
        self.__view = TotalWindowView(self, self.__model)
        self.__proxy = AdminPanelAPI()

    def load_total_report(self):
        data = {"id_contest": self.__model.select_contest.id,
                "state_contest": 0}
        is_send, response = self.__proxy.load_to_database_report_total(data)
        self.__model.total_report = response
        """BASE = "http://127.0.0.1:5000"
        response = requests.get(f"{BASE}/report_total/{Session().team.id}", {"id_report": 0})
        response = response.json()
        self.__model.total_report = response
        eel.loadTotalContest(self.__model.total_report)"""

    def load_contest(self):
        self.__view.update("contests")

    def show_view(self, contests):
        self.__model.contests = contests
        self.__view.show_view()

    def close_window(self):
        EelModification.close_window(self.__view.name_window)

    def set_select_contest(self, id_contest):
        self.__model.select_contest = id_contest
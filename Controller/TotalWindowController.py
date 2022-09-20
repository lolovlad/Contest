from typing import List

from View.TotalWindowView import TotalWindowView
from Classes.EelModification import EelModification
from Classes.ProxyController.ContestProxy import ContestProxy
from Model.TotalWindowModel import TotalWindowModel


class TotalWindowController:
    def __init__(self, model: TotalWindowModel = TotalWindowModel(), proxy: ContestProxy = ContestProxy()):
        self.__model = model
        self.__view = TotalWindowView(self, self.__model)
        self.__proxy = proxy

    def load_total_report(self, id_contest):
        is_send, response = self.__proxy.get_report_total(id_contest)
        if is_send:
            self.__model.total_report = response

    def load_contest(self):
        self.__view.update("contests")

    def show_view(self, contests: List[dict]):
        self.__model.contests = contests
        self.__view.show_view()

    def set_select_contest(self, id_contest):
        self.__model.select_contest = id_contest
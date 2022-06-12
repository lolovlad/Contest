import requests
from Classes.ProxyController.MenuProxy import MenuProxy
from Classes.Session import Session
from View.MenuView import MenuView
from json import dumps
from Classes.EelModification import EelModification


class MenuController:
    def __init__(self, model):
        self.__model = model
        self.__view = MenuView(self, self.__model)
        self.__proxy = MenuProxy()

    def show_view(self):
        self.__view.show_view()

    def default(self):
        pass

    def load_contest(self):
        data = {"id": 0,
                "additional_modifications": dumps({"type_contest": "to_id_team", "id_team": Session().user.team.id})}
        is_send, response = self.__proxy.load_to_database_contest(data)
        if is_send:
            self.__model.contests = response[1]["contests"]

    def get_select_contest(self, id_contest):
        return self.__model.select_contest(id_contest)

    def get_contest(self):
        return self.__model.contests

    def close_window(self):
        EelModification.close_window(self.__view.name_window)

import requests
from Classes.ProxyController.MenuProxy import MenuProxy
from Classes.Session import Session
from View.MenuView import MenuView
from json import dumps
from Classes.EelModification import EelModification
from Model.MenuModel import MenuModel


class MenuController:
    def __init__(self, model: MenuModel = MenuModel(), proxy: MenuProxy = MenuProxy()):
        self.__model: MenuModel = model
        self.__view: MenuView = MenuView(self, self.__model)
        self.__proxy: MenuProxy = proxy

    def show_view(self):
        self.__view.show_view()

    def default(self):
        pass

    def load_contest(self):
        data = {"id_user": Session().user.id}
        is_send, response = self.__proxy.load_to_database_contest(data)
        if is_send:
            self.__model.contests = response

    def get_select_contest(self, id_contest):
        return self.__model.select_contest(id_contest)

    def get_contest(self):
        return self.__model.contests

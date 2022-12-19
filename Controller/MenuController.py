import requests
from Classes.ProxyController.ContestProxy import ContestProxy
from Classes.Session import Session
from View.MenuView import MenuView
from json import dumps
from Classes.EelModification import EelModification
from Model.MenuModel import MenuModel


class MenuController:
    def __init__(self, model: MenuModel = MenuModel()):
        self.__model: MenuModel = model
        self.__view: MenuView = MenuView(self, self.__model)
        self.__proxy: ContestProxy = ContestProxy()

    def show_view(self):
        self.__view.show_view()

    def default(self):
        pass

    def load_contest(self):
        response = self.__proxy.contests_by_user_id(0)
        self.__model.contests = response

    def get_select_contest(self, id_contest):
        return self.__model.select_contest(id_contest)

    def get_contest(self):
        return self.__model.contests

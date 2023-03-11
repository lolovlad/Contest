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
        response = self.__proxy.contests_by_user_id()
        return response

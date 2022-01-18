import requests

from View.LoginView import LoginView
from Controller.MenuController import MenuController
from Model.MenuModel import MenuModel
from Classes.EelModification import EelModification
import eel


class LoginController:
    def __init__(self, model):
        self.__model = model
        self.__view = LoginView(self, self.__model)

    def show_view(self):
        self.__view.show_view()

    def login(self):
        '''new class'''
        BASE = "http://127.0.0.1:5000"
        response = requests.post(f"{BASE}/login", {"login": self.__model.login, "password": self.__model.password})
        response = response.json()
        if response.get("error") is None:
            print(response)
            EelModification.close_window('localhost:8000/login.html')
            if response["type"] == 1:
                menu_window = MenuController(MenuModel())
                menu_window.show_view()
            elif response["type"] == 2:
                pass
        else:
            self.__model.error = response["error"]

    def set_login(self, login):
        self.__model.login = login

    def set_password(self, password):
        self.__model.password = password



import requests

from View.LoginView import LoginView
from Classes.EelModification import EelModification
import eel


class LoginController:
    def __init__(self, model, controllers):
        self.__model = model
        self.__view = LoginView(self, self.__model)
        self.__controllers = controllers

    def show_view(self):
        self.__view.show_view()

    def login(self):
        '''new class'''
        BASE = "http://127.0.0.1:5000"
        response = requests.post(f"{BASE}/login", {"login": self.__model.login, "password": self.__model.password})
        response = response.json()
        if response.get("error") is None:
            self.__model.user = response
            if response["type"] == 1:
                EelModification.close_window('localhost:8000/login.html')
                self.__controllers.admin_panel.show_view()
            elif response["type"] == 2:
                EelModification.close_window('localhost:8000/login.html')
                self.__controllers.menu.show_view()
        else:
            self.__model.error = response["error"]

    def set_login(self, login):
        self.__model.login = login

    def set_password(self, password):
        self.__model.password = password



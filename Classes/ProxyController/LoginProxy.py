from typing import List

from Interfase.Proxy.Login import Login
from Classes.ProxyController.LoginAPI import LoginAPI
from functools import partial


class LoginProxy(Login):
    def __init__(self, login_api: LoginAPI = LoginAPI()):
        self.__login = login_api
        self.operations: List[object] = []

    def login(self, data):
        func = partial(self.__login.login, data)
        self.operations.append(func)

    def send(self):
        responses = list(map(lambda f: f(), self.operations))
        self.operations = []
        return responses[-1]

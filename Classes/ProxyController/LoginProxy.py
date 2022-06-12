from Interfase.Proxy.Login import Login
from Classes.ProxyController.LoginAPI import LoginAPI
from functools import partial


class LoginProxy(Login):
    def __init__(self):
        self.__login = LoginAPI()
        self.operations = []

    def login(self, data):
        func = partial(self.__login.login, data)
        self.operations.append(func)

    def send(self):
        try:
            response = list(map(lambda f: f(), self.operations))
            self.operations = []
            return response
        except Exception:
            return [(False, "ошибка в отправке данных")]

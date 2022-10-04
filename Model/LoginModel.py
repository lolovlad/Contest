from typing import List

from Interfase import Observer, Subject, Model
from Classes.Session import Session
from Classes.Models import Login
from Classes.Models.Login import Token


class LoginModel(Subject, Model):
    def __init__(self, token: Token = Token(), login: Login = Login()):
        self.__login: Login = login
        self.__error: str = ""
        self.__observer: List[Observer] = []
        self.__token: Token = token

    @property
    def login(self):
        return self.__login

    @property
    def token(self):
        return self.__token

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, val: str):
        self.__error = val
        self.notify()

    @login.setter
    def login(self, val: dict):
        self.__login = Login(**val)

    @token.setter
    def token(self, val: dict):
        self.__token = Token(**val)
        Session().token = self.__token

    def attach(self, observer: Observer):
        self.__observer.append(observer)

    def detach(self, observer: Observer):
        self.__observer.remove(observer)

    def notify(self, type_notify: str = None):
        for observer in self.__observer:
            observer.update(type_notify)
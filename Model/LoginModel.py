from typing import List

from Interfase import Observer, Subject, Model
from Classes.Session import Session
from Classes.Models import Login
from Classes.Models.User import UserUpdate as User


class LoginModel(Subject, Model):
    def __init__(self, user: User = User(), login: Login = Login()):
        self.__login: Login = login
        self.__error: str = ""
        self.__observer: List[Observer] = []
        self.__user: User = user

    @property
    def login(self):
        return self.__login

    @property
    def user(self):
        return self.__user

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

    @user.setter
    def user(self, val: dict):
        self.__user = User(**val)
        Session().user = self.__user

    def attach(self, observer: Observer):
        self.__observer.append(observer)

    def detach(self, observer: Observer):
        self.__observer.remove(observer)

    def notify(self, type_notify: str = None):
        for observer in self.__observer:
            observer.update(type_notify)
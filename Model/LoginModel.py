from Interfase.Subject import Subject
from Classes.Session import Session
from pykson import Pykson
from Classes.Models.User import User


class LoginModel(Subject):
    def __init__(self):
        self.__login = None
        self.__password = None
        self.__error = None
        self.__observer = []
        self.__user = None

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def user(self):
        return self.__user

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, val):
        self.__error = val
        self.notify()

    @login.setter
    def login(self, val):
        self.__login = val

    @password.setter
    def password(self, val):
        self.__password = val

    @user.setter
    def user(self, val):
        self.__user = Pykson().from_json(val, User)
        Session().user = self.__user

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self):
        for observer in self.__observer:
            observer.update()
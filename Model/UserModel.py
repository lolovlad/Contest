from typing import List

from Interfase import Subject, Observer
from Classes.Models.TypeNotify import TypeNotify
from Classes.Models.User import UserUpdate


class UserModel(Subject):
    def __init__(self):
        self.__observer: List[Observer] = []
        self.__select_id_user: int = 0
        self.__mode_update: bool = False
        self.__select_user: UserUpdate = UserUpdate()

    @property
    def mode_update(self):
        return self.__mode_update

    @mode_update.setter
    def mode_update(self, val):
        self.__mode_update = val

    @property
    def select_id_user(self):
        return self.__select_id_user

    @select_id_user.setter
    def select_id_user(self, id_user):
        self.__select_id_user = id_user

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify: TypeNotify, **kwargs):
        for observer in self.__observer:
            observer.update(type_notify, **kwargs)

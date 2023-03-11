from typing import List

from Interfase import Subject, Observer

import eel

from Classes.Models.TypeNotify import TypeNotify
from Classes.Models.Contest import ContestGet
from Classes.Models.Task import TaskPut, TaskGet
from datetime import datetime


class ContestModel(Subject):
    def __init__(self):
        self.__observer: List[Observer] = []
        self.__mode_update: bool = False
        self.__id_contest: int = 0

    @property
    def mode_update(self) -> bool:
        return self.__mode_update

    @mode_update.setter
    def mode_update(self, mode: bool):
        self.__mode_update = mode

    @property
    def id_contest(self) -> int:
        return self.__id_contest

    @id_contest.setter
    def id_contest(self, id_contest: int):
        self.__id_contest = id_contest

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify: TypeNotify, **kwargs):
        for observer in self.__observer:
            observer.update(type_notify, **kwargs)
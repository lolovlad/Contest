from typing import List

from Interfase import Subject, Observer
from Classes.Models.TypeNotify import TypeNotify
from Classes.Models.Team import TeamGet


class TeamModel(Subject):
    def __init__(self):
        self.__observer: List[Observer] = []
        self.__id_team: int = 0
        self.__mode_update: bool = False

    @property
    def id_team(self) -> int:
        return self.__id_team

    @id_team.setter
    def id_team(self, id_team: int):
        self.__id_team = id_team

    @property
    def mode_update(self) -> bool:
        return self.__mode_update

    @mode_update.setter
    def mode_update(self, mode_update: bool):
        self.__mode_update = mode_update

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify: TypeNotify):
        for observer in self.__observer:
            observer.update(type_notify)

from typing import List

from Interfase.Observer import Subject, Observer
from Classes.Models import Menu
from pykson import Pykson


class MenuModel(Subject):
    def __init__(self):
        self.__observer: List[Observer] = []
        self.__contests: List[Menu] = []

    @property
    def contests(self):
        contests = list(map(lambda x: x.dict(), self.__contests))
        for contest in contests:
            contest["contests"]["datetime_start"] = contest["contests"]["datetime_start"].isoformat()
            contest["contests"]["datetime_end"] = contest["contests"]["datetime_end"].isoformat()
            contest["contests"]["datetime_registration"] = contest["contests"]["datetime_registration"].isoformat()
        return contests

    @contests.setter
    def contests(self, val: List[dict]):
        self.__contests = list(map(lambda x: Menu(**x), val))
        self.notify("contests")

    def select_contest(self, contest: dict):
        return list(filter(lambda x: x.contests.id == contest["contests"]["id"], self.__contests))[0]

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify):
        for observer in self.__observer:
            observer.update(type_notify)
from Interfase.Subject import Subject
from Classes.Models.Contes import Contest
from pykson import Pykson


class MenuModel(Subject):
    def __init__(self):
        self.__observer = []
        self.__contests = []

    @property
    def contests(self):
        return list(map(Pykson().to_dict_or_list, self.__contests))

    @contests.setter
    def contests(self, val):
        self.__contests = list(map(lambda x: Pykson().from_json(x, Contest), val))
        self.notify("contests")

    def select_contest(self, id_contest):
        return list(filter(lambda x: x.id == id_contest, self.__contests))[0]

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify):
        for observer in self.__observer:
            observer.update(type_notify)
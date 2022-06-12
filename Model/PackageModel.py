from Interfase.Subject import Subject
from pykson import Pykson
from Classes.Models.Answer import Answer


class PackageModel(Subject):
    def __init__(self):
        self.__observer = []
        self.__answers = []
        self.__id_contest = None
        self.__select_report = None

    @property
    def answers(self):
        return list(map(Pykson().to_dict_or_list, self.__answers))

    @answers.setter
    def answers(self, val):
        if isinstance(val[0], Answer):
            self.__answers = val
        else:
            self.__answers = list(map(lambda x: Pykson().from_json(x, Answer), val))
        self.notify("answers")

    @property
    def id_contest(self):
        return self.__id_contest

    @id_contest.setter
    def id_contest(self, val):
        self.__id_contest = val

    @property
    def select_report(self):
        return self.__select_report

    @select_report.setter
    def select_report(self, val):
        self.__select_report = val
        self.notify("select_report")

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify):
        for observer in self.__observer:
            observer.update(type_notify)
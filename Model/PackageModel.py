from typing import List
from Interfase.Observer import Subject, Observer
from pykson import Pykson
from Classes.Models.Answer import AnswerGet
from Classes.Models.Report import Report


class PackageModel(Subject):
    def __init__(self):
        self.__observer: List[Observer] = []
        self.__answers: List[AnswerGet] = []
        self.__id_contest: int = 0
        self.__select_report: Report = Report()

    @property
    def answers(self):
        answers = []
        for answer in self.__answers:
            answer_target = answer.dict()
            answer_target["date_send"] = answer_target["date_send"].isoformat()
            answers.append(answer_target)
        return answers

    @answers.setter
    def answers(self, val: List[dict]):
        self.__answers.clear()
        for answer in val:
            self.__answers.append(AnswerGet(**answer))
        self.notify("answers")

    @property
    def id_contest(self):
        return self.__id_contest

    @id_contest.setter
    def id_contest(self, val: int):
        self.__id_contest = val

    @property
    def select_report(self):
        return self.__select_report.dict()

    @select_report.setter
    def select_report(self, val: dict):
        self.__select_report = Report(**val)
        self.notify("select_report")

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify):
        for observer in self.__observer:
            observer.update(type_notify)
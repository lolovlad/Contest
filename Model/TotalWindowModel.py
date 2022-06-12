from Interfase.Subject import Subject
from Classes.Models.Contes import Contest
from datetime import datetime
from pykson import Pykson


class TotalWindowModel(Subject):
    def __init__(self):
        self.__observer = []
        self.__total_report = None
        self.__contests = []
        self.__select_contest = None

    @property
    def total_report(self):
        return self.__total_report

    @total_report.setter
    def total_report(self, val):
        self.__total_report = val
        self.notify("report_contest")

    @property
    def contests(self):
        return list(map(Pykson().to_dict_or_list, self.__contests))

    @contests.setter
    def contests(self, val):
        for contest in val:
            for key in contest:
                contest[key] = self.__conver_datetime_field(contest[key])
        self.__contests = list(map(lambda x: Pykson().from_json(x, Contest), val))
        self.notify("contests")

    @property
    def select_contest(self):
        return self.__select_contest

    @select_contest.setter
    def select_contest(self, val):
        self.__select_contest = list(filter(lambda x: x.id == val, self.__contests))[0]
        self.notify("select_contest")


    def __conver_datetime_field(self, val):
        try:
            return datetime.fromisoformat(val)
        except Exception:
            return val

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        pass

    def notify(self, type_notify):
        for observer in self.__observer:
            observer.update(type_notify)

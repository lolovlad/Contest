from typing import List
from Interfase.Observer import Subject, Observer
from Classes.Models import Menu
from Classes.Models import ReportTotal
from datetime import datetime
from pykson import Pykson


class TotalWindowModel(Subject):
    def __init__(self):
        self.__observer: List[Observer] = []
        self.__total_report: List[ReportTotal] = []
        self.__contests: List[Menu] = []
        self.__select_contest: Menu = Menu()

    @property
    def total_report(self) -> List[dict]:
        reports_total = []
        for total_report in self.__total_report:
            total_report_target = total_report.dict()
            reports_total.append(total_report_target)
        return reports_total

    @total_report.setter
    def total_report(self, val: List[dict]):
        self.__total_report.clear()
        for report_total in val:
            self.__total_report.append(ReportTotal(**report_total))
        self.notify("report_contest")

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

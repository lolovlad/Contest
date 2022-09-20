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
        self.__select_contest: ContestGet = ContestGet()
        self.__select_task: TaskPut = TaskPut()
        self.__contests: List[ContestGet] = []

    @property
    def contests(self) -> List[ContestGet]:
        return self.__contests

    @contests.setter
    def contests(self, val: List[dict]):
        self.__contests.clear()
        for contest in val:
            self.__contests.append(ContestGet(**contest))
        self.notify(TypeNotify.CONTEST_TABLE)

    @property
    def select_contest(self) -> ContestGet:
        return self.__select_contest

    @select_contest.setter
    def select_contest(self, val: dict):
        self.__select_contest = list(filter(lambda x: x.id == val["id"], self.__contests))[0]
        print(self.__select_contest)
        self.notify(TypeNotify.CONTEST_FORM)

    def clear_select_contest(self):
        self.__select_contest = ContestGet()

    def json_select_contest(self) -> dict:
        contest = self.__select_contest.dict()
        contest["datetime_start"] = contest["datetime_start"].isoformat()
        contest["datetime_end"] = contest["datetime_end"].isoformat()
        contest["datetime_registration"] = contest["datetime_registration"].isoformat()
        return contest

    def dict_contest(self, contest) -> dict:
        contest = contest.dict()
        try:
            contest["datetime_start"] = contest["datetime_start"].strftime("%d.%m.%Y, %H:%M")
            contest["datetime_end"] = contest["datetime_end"].strftime("%d.%m.%Y, %H:%M")
            contest["datetime_registration"] = contest["datetime_registration"].strftime("%d.%m.%Y, %H:%M")
        except Exception:
            contest["datetime_registration"] = contest["datetime_registration"].strftime("%d.%m.%Y, %H:%M")
        return contest

    def update_select_contest(self, contest: dict):
        try:
            contest_old = self.__select_contest.dict()
            for key in contest:
                contest_old[key] = contest[key]
            self.__select_contest = ContestGet(**contest_old)
        except ValueError as e:
            #eel.errorUpdateFieldUser(e)
            pass

    def add_contest(self, val: dict):
        self.__contests.append(ContestGet(**val))
        self.notify(TypeNotify.CONTEST_TABLE)

    def delete_contest(self, val):
        for i, contest in enumerate(self.__contests):
            if contest.id == val["id"]:
                self.__contests.pop(i)
                break
        self.notify(TypeNotify.CONTEST_TABLE)

    def update_contest(self, val):
        for i, contest in enumerate(self.__contests):
            if contest.id == val["id"]:
                self.__contests[i] = ContestGet(**val)
                break
        self.notify(TypeNotify.CONTEST_TABLE)

    @property
    def select_task(self) -> TaskPut:
        return self.__select_task

    @select_task.setter
    def select_task(self, val: dict):
        self.__select_task = list(filter(lambda x: x.id == val["id"], self.__select_contest.tasks))[0]
        self.notify(TypeNotify.TASK_FORM)

    def clear_select_task(self):
        self.__select_task = TaskPut()

    def update_select_task(self, task: dict):
        try:
            task_old = self.__select_task.dict()
            for key in task:
                task_old[key] = task[key]
            self.__select_task = TaskPut(**task_old)
            print(self.__select_task)
        except ValueError as e:
            #eel.errorUpdateFieldUser(e)
            pass

    def add_task(self, val):
        self.__select_contest.tasks.append(TaskGet(**val))
        self.update_contest(self.json_select_contest())
        self.notify(TypeNotify.TASK_TABLE)

    def delete_task(self, val):
        for i, task in enumerate(self.__select_contest.tasks):
            if task.id == val["id"]:
                self.__select_contest.tasks.pop(i)
                break
        self.update_contest(self.json_select_contest())
        self.notify(TypeNotify.TASK_TABLE)

    def update_task(self, val):
        for i, task in enumerate(self.__select_contest.tasks):
            if task.id == val["id"]:
                self.__select_contest.tasks[i] = TaskGet(**val)
                break
        self.update_contest(self.json_select_contest())
        self.notify(TypeNotify.TASK_TABLE)

    def tasks(self):
        self.notify(TypeNotify.TASK_TABLE)

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify: TypeNotify):
        for observer in self.__observer:
            observer.update(type_notify)
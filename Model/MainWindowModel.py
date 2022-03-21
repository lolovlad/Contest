from Interfase.Subject import Subject
from Classes.Models.Task import Task
from pykson import Pykson


class MainWindowModel(Subject):
    def __init__(self):
        self.__observer = []
        self.__tasks = {}
        self.__id_contest = 1
        self.__select_task = None
        self.__answers = {}
        self.__file = None

    @property
    def id_contest(self):
        return self.__id_contest

    @id_contest.setter
    def id_contest(self, val):
        self.__id_contest = val
        self.notify()

    @property
    def tasks(self):
        return self.__tasks

    @tasks.setter
    def tasks(self, val):
        self.__tasks = val

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, val):
        self.__file = val

    @property
    def answers(self):
        return self.__answers

    @answers.setter
    def answers(self, val):
        self.__answers = val

    def get_select_task(self, id_task):
        for task in self.__tasks:
            if task["id"] == id_task:
                self.__select_task = task
                break

    @property
    def select_task(self):
        return self.__select_task

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self):
        for observer in self.__observer:
            observer.update()
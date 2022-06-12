from Interfase.Subject import Subject
from Classes.Models.Task import Task
from Classes.Models.Contes import Contest
from Classes.Models.Answer import Answer
from pykson import Pykson


class MainWindowModel(Subject):
    def __init__(self):
        self.__observer = []
        self.__tasks = []
        self.__files = {}
        self.__contest = Contest()
        self.__select_task = Task()
        self.__select_answers = []
        self.__select_report = None
        self.__answers = []
        self.__menu = {}
        self.__file = None

    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, val):
        self.__files = val

    @property
    def contest(self):
        return Pykson().to_dict_or_list(self.__contest)

    @contest.setter
    def contest(self, val):
        self.__contest = val
        self.tasks = self.__contest.tasks
        self.notify("contests")

    @property
    def tasks(self):
        return list(map(Pykson().to_dict_or_list, self.__tasks))

    @tasks.setter
    def tasks(self, val):
        if isinstance(val[0], Task):
            self.__tasks = val
        else:
            self.__tasks = list(map(lambda x: Pykson().from_json(x, Task), val))
        self.notify("tasks")

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, val):
        self.__file = val

    @property
    def select_answers(self):
        return Pykson().to_dict_or_list(self.__select_answers)

    @select_answers.setter
    def select_answers(self, val):
        self.__select_answers = list(map(lambda x: Pykson().from_json(x, Answer), val))
        self.notify("select_answers")

    @property
    def select_report(self):
        return self.__select_report

    @select_report.setter
    def select_report(self, val):
        self.__select_report = val
        self.notify("select_report")

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, val):
        self.__menu = val
        self.notify("menu")

    @property
    def select_task(self):
        return Pykson().to_dict_or_list(self.__select_task)

    @select_task.setter
    def select_task(self, val):
        for task in self.__tasks:
            if task.id == val:
                self.__select_task = task
                self.notify("select_task")
                break

    def id_list_task(self):
        return [i.id for i in self.__tasks]

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self,  type_notify):
        for observer in self.__observer:
            observer.update(type_notify)
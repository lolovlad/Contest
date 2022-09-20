from typing import List
from Classes.Models.Task import TaskGet, TaskPage
from Classes.Models.Contest import ContestGetPage
from Interfase.Observer import Subject, Observer
from Classes.Models.Answer import AnswerGet, AnswerPost
from Classes.Models.Report import Report
from pykson import Pykson


class MainWindowModel(Subject):
    def __init__(self):
        self.__id_contest: int = 0
        self.__contest: ContestGetPage = ContestGetPage()
        self.__observer: List[Observer] = []
        self.__tasks: List[TaskPage] = []
        self.__files = {}
        self.__select_task: TaskPage = TaskPage()
        self.__select_answer: AnswerPost = AnswerPost()
        self.__select_report: Report = Report()
        self.__answers: List[AnswerGet] = []
        self.__menu: dict = {}
        self.__file: dict = {}

    @property
    def id_contest(self):
        return self.__id_contest

    @id_contest.setter
    def id_contest(self, val: int):
        self.__id_contest = val

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, val: dict):
        print(val)
        self.__file = val

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, val: dict):
        self.__menu = val
        self.notify("menu")

    @property
    def contest(self) -> dict:
        contest = self.__contest.dict()
        contest["datetime_start"] = contest["datetime_start"].isoformat()
        contest["datetime_end"] = contest["datetime_end"].isoformat()
        contest["datetime_registration"] = contest["datetime_registration"].isoformat()
        return contest

    @contest.setter
    def contest(self, val: dict):
        self.__contest = ContestGetPage(**val)
        self.tasks = self.__contest.tasks
        self.notify("contests")

    @property
    def tasks(self):
        return list(map(Pykson().to_dict_or_list, self.__tasks))

    @tasks.setter
    def tasks(self, val: List[TaskGet]):
        self.__tasks = val
        self.notify("tasks")

    @property
    def select_answer(self):
        return self.__select_answer.dict()

    @select_answer.setter
    def select_answer(self, val: dict):
        try:
            answer_old = self.__select_answer.dict()
            for key in val:
                answer_old[key] = val[key]
            self.__select_answer = AnswerPost(**answer_old)
        except ValueError as e:
            #eel.errorUpdateFieldUser(e)
            pass

    @property
    def select_report(self) -> dict:
        return self.__select_report.dict()

    @select_report.setter
    def select_report(self, val: dict):
        self.__select_report = Report(**val)
        self.notify("select_report")

    @property
    def answers(self) -> List[dict]:
        answers = []
        for answer in self.__answers:
            answer_target = answer.dict()
            answer_target["date_send"] = answer_target["date_send"].isoformat()
            answers.append(answer_target)
        return answers

    @answers.setter
    def answers(self, val: dict):
        self.__answers.clear()
        for answer in val:
            self.__answers.append(AnswerGet(**answer))
        self.notify("select_answers")

    def add_answer(self, val: dict):
        self.__answers.append(AnswerGet(**val))
        self.notify("select_answers")

    @property
    def select_task(self):
        return self.__select_task.dict()

    @select_task.setter
    def select_task(self, val: int):
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
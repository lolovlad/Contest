from Interfase.Subject import Subject
from Classes.Models.User import User
from Classes.Models.Contes import Contest
from Classes.Models.Task import Task
import datetime
from pykson import Pykson


class AdminPanelModel(Subject):
    def __init__(self):
        self.__observer = []
        self.__users = []
        self.__select_user = User()
        self.__select_contest = Contest()
        self.__tasks = {}

    def add_user(self, val):
        self.__users.append(val)
        self.notify()

    def delete_user(self, val):
        for user_num in range(len(self.__users)):
            if self.__users[user_num].id == val.id:
                self.__users.pop(user_num)
                self.notify()
                return

    def update_tasks(self, val):
        self.__tasks[val["num_task"]] = val["data"]

    def add_tasks(self, val):
        self.__tasks[val["num_task"]] = val["date"]

    @property
    def select_user(self):
        return self.__select_user

    @select_user.setter
    def select_user(self, val):
        self.__select_user = Pykson().from_json(val, User)
        self.notify()

    @property
    def select_contest(self):
        return self.__select_contest

    @select_contest.setter
    def select_contest(self, val):
        start_datetime = datetime.datetime(val["dateStart"]["year"], val["dateStart"]["month"], val["dateStart"]["day"],
                                           val["timeStart"]["hours"],  val["timeStart"]["min"], 0)
        end_datetime = datetime.datetime(val["dateEnd"]["year"], val["dateEnd"]["month"], val["dateEnd"]["day"],
                                         val["timeEnd"]["hours"], val["timeEnd"]["min"], 0)
        val = {"id": val["id"],
               "name_contest": val["nameContest"],
               "type": val["typeSelectedContes"],
               "datetime_start": start_datetime,
               "datetime_end": end_datetime}
        self.__select_contest = Pykson().from_json(val, Contest)
        print(val)
        self.notify()

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self):
        for observer in self.__observer:
            observer.update()
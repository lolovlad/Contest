import requests
from View.AdminPanelView import AdminPanelView
from Classes.TabContest import TabContest
from Classes.TabTask import TabTask
import eel
from pykson import Pykson
from json import loads


class AdminPanelController:
    def __init__(self, model):
        self.__model = model
        self.__view = AdminPanelView(self, self.__model)
        self.__tab_contest = TabContest(self.__model)
        self.__tab_task = TabTask(self.__model)

    def show_view(self):
        self.__view.show_view()

    def default(self):
        pass

    def add_user(self):
        BASE = "http://127.0.0.1:5000"
        user = loads(Pykson().to_json(self.__model.select_user))
        response = requests.post(f"{BASE}/registration", user)
        response = response.json()
        if response.get("error") is None:
            print("ok")
            self.load_users()
        else:
            print(response["error"])

    def update_user(self):
        BASE = "http://127.0.0.1:5000"
        user = loads(Pykson().to_json(self.__model.select_user))
        response = requests.put(f"{BASE}/users/{self.__model.select_user.id}", data=user)
        response = response.json()
        self.load_users()
        print(response)

    def delete_user(self):
        BASE = "http://127.0.0.1:5000"
        response = requests.delete(f"{BASE}/users/{self.__model.select_user.id}")
        response = response.json()
        self.load_users()
        print(response)

    def load_users(self):
        BASE = "http://127.0.0.1:5000"
        response = requests.post(f"{BASE}/load_users")
        response = response.json()
        eel.updateTable(response)

    def load_contest(self):
        BASE = "http://127.0.0.1:5000"
        response = requests.get(f"{BASE}/contests/1")
        response = response.json()
        eel.updateTableContest(response)

    def load_tasks(self):
        BASE = "http://127.0.0.1:5000"
        response = requests.get(f"{BASE}/tasks/{self.__model.select_contest.id}")
        response = response.json()
        self.__model.tasks = response["tasks"]
        eel.updateTableTasks(response)

    def add_contest(self):
        self.__tab_contest.add_contest()

    def delete_contest(self):
        self.__tab_contest.delete_contest()
        self.load_contest()

    def update_contest(self):
        self.__tab_contest.update_contest()
        self.load_contest()

    def add_task(self):
        self.__tab_task.add_task()
        self.load_tasks()

    def delete_task(self):
        self.__tab_task.delete_task()
        self.load_tasks()

    def update_task(self):
        self.__tab_task.update_task()
        self.load_tasks()

    def set_select_user(self, user):
        self.__model.select_user = user

    def set_select_contest(self, contest):
        self.__model.select_contest = contest

    def update_tasks(self, tasks):
        self.__model.select_task = tasks

    def select_task(self, id_task):
        for task in self.__model.tasks:
            print(task)
            if task["id"] == id_task:
                return task


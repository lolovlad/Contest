from json import loads, dumps
import requests
from pykson import Pykson


class TabTask:
    def __init__(self, model):
        self.__model = model

    def add_task(self):
        BASE = "http://127.0.0.1:5000"
        task = {}
        task = loads(Pykson().to_json(self.__model.select_task))
        task["json"] = open(self.__model.select_task.path_test_file, "rb").read().decode("utf-8")
        task["py"] = open(self.__model.select_task.path_programme_file, "rb").read().decode("utf-8")
        response = requests.post(f"{BASE}/tasks/{self.__model.select_contest.id}", {"data": dumps(task)})
        response = response.json()
        if response.get("error") is None:
            print("ok")
        else:
            print(response["error"])

    def delete_task(self):
        BASE = "http://127.0.0.1:5000"
        response = requests.delete(f"{BASE}/tasks/{self.__model.select_task.id}")
        response = response.json()
        print(response)

    def update_task(self):
        BASE = "http://127.0.0.1:5000"
        task = {}
        task = loads(Pykson().to_json(self.__model.select_task))
        try:
            task["json"] = open(self.__model.select_task.path_test_file, "rb").read().decode("utf-8")
        except Exception:
            pass
        try:
            task["py"] = open(self.__model.select_task.path_programme_file, "rb").read().decode("utf-8")
        except Exception:
            pass
        response = requests.put(f"{BASE}/tasks/{self.__model.select_task.id}", {"data": dumps(task)})
        response = response.json()
        print(response)
from json import loads
import requests
from pykson import Pykson


class TabContest:
    def __init__(self, model):
        self.__model = model

    def add_contest(self):
        BASE = "http://127.0.0.1:5000"
        contest = loads(Pykson().to_json(self.__model.select_contest))
        response = requests.post(f"{BASE}/contests/1", contest)
        response = response.json()
        if response.get("error") is None:
            print("ok")
        else:
            print(response["error"])

    def delete_contest(self):
        BASE = "http://127.0.0.1:5000"
        response = requests.delete(f"{BASE}/contests/{self.__model.select_contest.id}")
        response = response.json()
        print(response)

    def update_contest(self):
        BASE = "http://127.0.0.1:5000"
        contest = loads(Pykson().to_json(self.__model.select_contest))
        response = requests.put(f"{BASE}/contests/{self.__model.select_contest.id}", data=contest)
        response = response.json()
        print(response)
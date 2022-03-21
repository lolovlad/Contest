import requests
from Classes.Session import Session
from View.MainWindowView import MainWindowView
from json import dumps, loads
import eel


class MainWindowController:
    def __init__(self, model):
        self.__model = model
        self.__view = MainWindowView(self, self.__model)

    def show_view(self, id_contest):
        self.__view.show_view(id_contest)

    def default(self):
        pass

    def load_contest(self):
        BASE = "http://127.0.0.1:5000"
        response = requests.get(f"{BASE}/contests/{self.__model.id_contest}")
        response = response.json()
        eel.loadsLeftInformation(response["contests"][0])

    def load_tasks_on_contest(self):
        BASE = "http://127.0.0.1:5000"
        response = requests.get(f"{BASE}/tasks/{self.__model.id_contest}")
        response_task = response.json()
        response = requests.get(f"{BASE}/json/{self.__model.id_contest}")
        response_json = response.json()
        for i in range(len(response_json["jsons_view"])):
            response_task["tasks"][i]["path_test_file"] = response_json["jsons_view"][i]
        self.__model.tasks = response_task["tasks"]
        eel.loadsTasks(self.__model.tasks)

    def load_answer(self):
        BASE = "http://127.0.0.1:5000"
        response = requests.get(f"{BASE}/answer/{self.__model.select_task['id']}")
        response = response.json()
        self.__model.answers = response
        eel.loadsAnswers(self.__model.answers)

    def load_report(self, id_report):
        BASE = "http://127.0.0.1:5000"
        response = requests.get(f"{BASE}/report/{id_report}")
        response = loads(response.json())
        eel.loadsReports(response)

    def upload_task(self, id_task):
        self.__model.get_select_task(id_task)
        return self.__model.select_task

    def send_answer(self):
        BASE = "http://127.0.0.1:5000"
        answer = {
            "extension_file": "py",
            "user_id": Session().user.id
        }

        try:
            answer["file"] = open(self.__model.file, "rb").read().decode("utf-8")
        except Exception:
            pass
        response = requests.post(f"{BASE}/answer/{self.__model.select_task['id']}", {"data": dumps(answer)})
        response = response.json()
        if response.get("error") is None:
            print("ok")
            self.load_answer()
        else:
            print(response["error"])

    def set_file(self, path_file):
        self.__model.file = path_file



    '''def set_login(self, login):
        self.__model.login = login

    def set_password(self, password):
        self.__model.password = password'''
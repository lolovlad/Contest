from Interfase.Proxy.Main import Main
from Classes.ProxyController.MainAPI import MainAPI
from functools import partial


class MainProxy(Main):

    def __init__(self):
        self.__api = MainAPI()
        self.operations = []

    def load_to_database_json_test_file(self, data):
        try:
            return True, self.__api.load_to_database_json_test_file(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def load_to_database_answers(self, data):
        try:
            return True, self.__api.load_to_database_answers(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def load_to_database_json_report(self, data):
        try:
            return True, self.__api.load_to_database_json_report(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def add_answer(self, data):
        func = partial(self.__api.add_answer, data)
        self.operations.append(func)
        return func()

    def update_team(self, data):
        func = partial(self.__api.update_team, data)
        self.operations.append(func)
        return func()
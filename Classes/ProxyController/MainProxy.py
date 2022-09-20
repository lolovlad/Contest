from Interfase.Proxy.Main import Main
from Classes.ProxyController.MainAPI import MainAPI
from functools import partial


class MainProxy(Main):

    def __init__(self, api: MainAPI = MainAPI()):
        self.__api = api
        self.operations = []

    def load_to_database_contest_page(self, data: dict):
        try:
            return True, self.__api.load_to_database_contest_page(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def load_to_database_package(self, data: dict):
        try:
            return True, self.__api.load_to_database_package(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def load_to_database_answers(self, data: dict):
        try:
            return True, self.__api.load_to_database_answers(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def load_to_database_json_report(self, data):
        try:
            return True, self.__api.load_to_database_json_report(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def load_to_database_compilation(self, data: dict):
        try:
            return True, self.__api.load_to_database_compilation(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def add_answer(self, data: dict):
        func = partial(self.__api.add_answer, data)
        self.operations.append(func)
        return func()

    def get_status_user(self, data: dict):
        func = partial(self.__api.get_status_user, data)
        self.operations.append(func)
        return func()

    def close_contest_to_user(self, data: dict):
        func = partial(self.__api.close_contest_to_user, data)
        self.operations.append(func)
        return func()

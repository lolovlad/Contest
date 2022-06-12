from Interfase.Proxy.AdminPanel import AdminPanel
from Classes.ProxyController.AdminPanelAPI import AdminPanelAPI
from functools import partial


class AdminPanelProxy(AdminPanel):

    def __init__(self):
        self.__api = AdminPanelAPI()
        self.operations = []

    def add_user(self, data):
        func = partial(self.__api.add_user, data)
        self.operations.append(func)
        return func()

    def delete_user(self, data):
        func = partial(self.__api.delete_user, data)
        self.operations.append(func)
        return func()

    def update_user(self, data):
        func = partial(self.__api.update_user, data)
        self.operations.append(func)
        return func()

    def load_to_database_user(self, data):
        try:
            return True, self.__api.load_to_database_user(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def add_contest(self, data):
        func = partial(self.__api.add_contest, data)
        self.operations.append(func)
        return func()

    def delete_contest(self, data):
        func = partial(self.__api.delete_contest, data)
        self.operations.append(func)
        return func()

    def update_contest(self, data):
        func = partial(self.__api.update_contest, data)
        self.operations.append(func)
        return func()

    def load_to_database_contest(self, data):
        try:
            return True, self.__api.load_to_database_contest(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def add_task(self, data):
        func = partial(self.__api.add_task, data)
        self.operations.append(func)
        return func()

    def delete_task(self, data):
        func = partial(self.__api.delete_task, data)
        self.operations.append(func)
        return func()

    def update_task(self, data):
        func = partial(self.__api.update_task, data)
        self.operations.append(func)
        return func()

    def load_to_database_team(self, data):
        try:
            return True, self.__api.load_to_database_team(data)
        except Exception:
            return False, "ошибка в отправке данных"

    def add_team(self, data):
        func = partial(self.__api.add_team, data)
        self.operations.append(func)
        return func()

    def delete_team(self, data):
        func = partial(self.__api.delete_team, data)
        self.operations.append(func)
        return func()

    def update_team(self, data):
        func = partial(self.__api.update_team, data)
        self.operations.append(func)
        return func()

    def load_to_database_report_total(self, data):
        try:
            return True, self.__api.load_to_database_report_total(data)
        except Exception:
            return False, "ошибка в отправке данных"
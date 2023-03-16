from Interfase.Proxy.UserContestView import UserContestView
from Classes.ProxyController.UserContestViewAPI import UserContestViewAPI
from functools import partial


class UserContestViewProxy(UserContestView):
    def __init__(self):
        self.__api: UserContestViewAPI = UserContestViewAPI()
        self.operations = []

    def get_contest(self, id_contest: int):
        func = partial(self.__api.get_contest, id_contest)
        self.operations.append(func)
        return func()

    def get_list_task(self, id_contest: int):
        func = partial(self.__api.get_list_task, id_contest)
        self.operations.append(func)
        return func()

    def get_task(self, id_task: int):
        func = partial(self.__api.get_task, id_task)
        self.operations.append(func)
        return func()

    def get_list_answers(self, id_contest: int, id_task: int):
        func = partial(self.__api.get_list_answers, id_contest, id_task)
        self.operations.append(func)
        return func()

    def get_report(self, id_answer: int):
        func = partial(self.__api.get_report, id_answer)
        self.operations.append(func)
        return func()

    def close_contest(self, id_contest: int):
        func = partial(self.__api.close_contest, id_contest)
        self.operations.append(func)
        return func()


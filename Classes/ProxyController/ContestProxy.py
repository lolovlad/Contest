from Interfase.Proxy.Contest import Contest
from Classes.ProxyController.ContestAPI import ContestAPI
from Classes.Models.Contest import ContestGet, ContestPost, ContestPutUsers
from functools import partial


class ContestProxy(Contest):
    def __init__(self, api: ContestAPI = ContestAPI()):
        self.__api = api
        self.operations = []

    def get_list_contest(self):
        func = partial(self.__api.get_list_contest)
        self.operations.append(func)
        return func()

    def post_contest(self, contest: dict):
        func = partial(self.__api.post_contest, contest)
        self.operations.append(func)
        return func()

    def delete_contest(self, id_contest: int):
        func = partial(self.__api.delete_contest, id_contest)
        self.operations.append(func)
        return func()

    def update_contest(self, contest: dict):
        func = partial(self.__api.update_contest, contest)
        self.operations.append(func)
        return func()

    def registration_users_contest(self, contest: ContestPutUsers):
        func = partial(self.__api.registration_users_contest, contest)
        self.operations.append(func)
        return func()

    def contests_by_user_id(self, id_user: int):
        func = partial(self.__api.contests_by_user_id, id_user)
        self.operations.append(func)
        return func()

    def contest_page(self, id_contest: int):
        func = partial(self.__api.contest_page, id_contest)
        self.operations.append(func)
        return func()

    def close_to_user_contest(self, id_contest: int, id_user: int):
        func = partial(self.__api.close_to_user_contest, id_contest, id_user)
        self.operations.append(func)
        return func()

    def get_report_total(self, id_contest: int):
        func = partial(self.__api.get_report_total, id_contest)
        self.operations.append(func)
        return func()



from Interfase.Proxy.User import User
from Classes.ProxyController.UserAPI import UserAPI
from Classes.Models.User import UserPost, UserUpdate
from functools import partial
from Classes.Models.Login import Token


class UserProxy(User):
    def __init__(self):
        self.__api: UserAPI = UserAPI()
        self.operations = []

    def get_users(self, params: dict):
        func = partial(self.__api.get_users, params)
        self.operations.append(func)
        return func()

    def get_user(self, id_user: int):
        func = partial(self.__api.get_user, id_user)
        self.operations.append(func)
        return func()

    def get_status_user(self, id_contest: int, id_user: int):
        data = {
            "id_contest": id_contest,
            "id_user": id_user
        }
        func = partial(self.__api.get_status_user, data)
        self.operations.append(func)
        return func()

    def post_user(self, user: UserPost):
        func = partial(self.__api.post_user, user)
        self.operations.append(func)
        return func()

    def put_user(self, user: UserUpdate):
        func = partial(self.__api.put_user, user)
        self.operations.append(func)
        return func()

    def delete_user(self, id_user: int):
        func = partial(self.__api.delete_user, id_user)
        self.operations.append(func)
        return func()

    def get_in_team_users(self, id_team: int):
        func = partial(self.__api.get_in_team_users, id_team)
        self.operations.append(func)
        return func()

    def get_in_contest_users(self, id_contest: int):
        func = partial(self.__api.get_in_contest_users, id_contest)
        self.operations.append(func)
        return func()

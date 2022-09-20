from typing import List

from Interfase import Subject, Observer
from Classes.Models.TypeNotify import TypeNotify
from Classes.Models.User import UserUpdate


class UserModel(Subject):
    def __init__(self):
        self.__observer: List[Observer] = []
        self.__select_user: UserUpdate = UserUpdate()
        self.__users: List[UserUpdate] = []

    @property
    def users(self) -> List[UserUpdate]:
        return self.__users

    @users.setter
    def users(self, val: List[dict]):
        self.__users.clear()
        for user in val:
            self.__users.append(UserUpdate(**user))
        self.notify(TypeNotify.USER_TABLE)

    @property
    def select_user(self) -> UserUpdate:
        return self.__select_user

    @select_user.setter
    def select_user(self, val: dict):
        self.__select_user = list(filter(lambda x: x.id == val["id"], self.__users))[0]
        self.notify(TypeNotify.USER_FORM)

    def clear_select_user(self):
        self.__select_user = UserUpdate()

    def update_select_user(self, user: dict):
        try:
            user_dict = self.__select_user.dict()
            for key in user:
                user_dict[key] = user[key]
            self.__select_user = UserUpdate(**user_dict)
            print(self.__select_user)
        except ValueError as e:
            #eel.errorUpdateFieldUser(e)
            pass

    def add_user(self, user: dict):
        self.__users.append(UserUpdate(**user))
        self.notify(TypeNotify.USER_TABLE)

    def delete_user(self, user: dict):
        for i, _user in enumerate(self.__users):
            if _user.id == user["id"]:
                self.__users.pop(i)
                break
        self.notify(TypeNotify.USER_TABLE)

    def update_user(self, user: dict):
        for i, _user in enumerate(self.__users):
            if _user.id == user["id"]:
                self.__users[i] = UserUpdate(**user)
                break
        self.notify(TypeNotify.USER_TABLE)

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify: TypeNotify):
        for observer in self.__observer:
            observer.update(type_notify)

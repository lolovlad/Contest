from Interfase.Subject import Subject


class AdminPanelModel(Subject):
    def __init__(self):
        self.__observer = []
        self.__users = []
        self.__select_user = None

    def add_user(self, val):
        self.__users.append(val)

    def delete_user(self, val):
        for user_num in range(len(self.__users)):
            if self.__users[user_num].id == val.id:
                self.__users.pop(user_num)
                return

    @property
    def select_user(self):
        return self.__select_user

    @select_user.setter
    def select_user(self, val):
        self.__select_user = val

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self):
        for observer in self.__observer:
            observer.update()
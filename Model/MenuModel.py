from Interfase.Subject import Subject


class MenuModel(Subject):
    def __init__(self):
        self.__observer = []
        self.__contests = []

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self):
        for observer in self.__observer:
            observer.update()
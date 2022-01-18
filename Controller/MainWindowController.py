import requests

from View.MainWindowView import MainWindowView
import eel


class MainWindowController:
    def __init__(self, model):
        self.__model = model
        self.__view = MainWindowView(self, self.__model)

    def show_view(self):
        self.__view.show_view()

    def default(self):
        pass

    '''def set_login(self, login):
        self.__model.login = login

    def set_password(self, password):
        self.__model.password = password'''
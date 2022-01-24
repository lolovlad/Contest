import requests
from View.AdminPanelView import AdminPanelView
import eel


class AdminPanelController:
    def __init__(self, model):
        self.__model = model
        self.__view = AdminPanelView(self, self.__model)

    def show_view(self):
        self.__view.show_view()

    def default(self):
        pass

    def add_user(self):
        print(123)

    def load_users(self):
        pass

    '''def set_login(self, login):
        self.__model.login = login

    def set_password(self, password):
        self.__model.password = password'''
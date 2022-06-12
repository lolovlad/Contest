from Interfase.Proxy.Menu import Menu
from Classes.ProxyController.MenuAPI import MenuAPI
from functools import partial


class MenuProxy(Menu):

    def __init__(self):
        self.__api = MenuAPI()
        self.operations = []

    def load_to_database_contest(self, data):
        try:
            return True, self.__api.load_to_database_contest(data)
        except Exception:
            return False, "ошибка в отправке данных"
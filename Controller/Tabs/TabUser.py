from json import loads, dumps
from pykson import Pykson


class TabUser:
    def __init__(self, model, proxy):
        self.__model = model
        self.__admin_panel_proxy = proxy

    def add_user(self):
        user = Pykson().to_dict_or_list(self.__model.select_user)
        return self.__admin_panel_proxy.add_user(user)

    def update_user(self):
        user = Pykson().to_dict_or_list(self.__model.select_user)
        return self.__admin_panel_proxy.update_user(user)

    def delete_user(self):
        user = Pykson().to_dict_or_list(self.__model.select_user)
        return self.__admin_panel_proxy.delete_user(user)

    def load_users(self):
        return self.__admin_panel_proxy.load_to_database_user({})

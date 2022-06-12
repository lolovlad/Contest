from json import loads, dumps
import requests
from pykson import Pykson


class TabTask:
    def __init__(self, model, proxy):
        self.__model = model
        self.__admin_panel_proxy = proxy

    def add_task(self):
        task = Pykson().to_dict_or_list(self.__model.select_task)
        task["json"] = open(self.__model.select_task.path_test_file, "rb").read().decode("utf-8")
        return self.__admin_panel_proxy.add_task({"data": dumps(task)})

    def delete_task(self):
        task = Pykson().to_dict_or_list(self.__model.select_task)
        return self.__admin_panel_proxy.delete_task(task)

    def update_task(self):
        task = Pykson().to_dict_or_list(self.__model.select_task)
        try:
            task["json"] = open(self.__model.select_task.path_test_file, "rb").read().decode("utf-8")
        except Exception:
            pass
        return self.__admin_panel_proxy.update_task({"data": dumps(task)})
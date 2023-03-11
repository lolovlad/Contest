from Classes.ProxyController import ContestProxy
import eel


class TotalPage:
    def __init__(self):
        self.__file_templates: dict = {
            "main": "templates/total.html",
        }
        self.__proxy: ContestProxy = ContestProxy()

    def show_view(self, **kwargs):
        eel.locationReplace(self.__file_templates["main"])

    def load_contest(self):
        return self.__proxy.get_list_contest()

    def load_total_report(self, id_contest: int):
        return self.__proxy.get_report_total(id_contest)

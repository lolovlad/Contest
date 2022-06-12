from json import dumps
import requests
from pykson import Pykson

from tkinter import filedialog
from tkinter import *

from Classes.BuilderFile.ReportXlsx import ReportXlsx


class TabContest:
    def __init__(self, model, proxy):
        self.__model = model
        self.__admin_panel_proxy = proxy

    def add_contest(self):
        contest = Pykson().to_dict_or_list(self.__model.contest_select)
        return self.__admin_panel_proxy.add_contest(contest)

    def load_contests(self, mode):
        data = {"id": 0,
                "additional_modifications": dumps({"type_contest": mode})}
        return self.__admin_panel_proxy.load_to_database_contest(data)

    def delete_contest(self):
        contest = Pykson().to_dict_or_list(self.__model.contest_select)
        return self.__admin_panel_proxy.delete_contest(contest)

    def update_contest(self):
        contest = Pykson().to_dict_or_list(self.__model.contest_select)
        return self.__admin_panel_proxy.update_contest(contest)

    def create_report(self):
        data = {"id_contest": self.__model.contest_select.id,
                "state_contest": 0}
        is_send, response = self.__admin_panel_proxy.load_to_database_report_total(data)
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        file = ReportXlsx(response[1])
        file.build_main_body()
        file.build_name_column()
        file.file.return_file(f"{folder_selected}/{self.__model.contest_select.name_contest}.xlsx")

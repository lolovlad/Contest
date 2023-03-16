from typing import List
from Classes.ProxyController import ContestProxy, TaskProxy, UserProxy, TeamProxy

from Classes.Models.Contest import ContestGet, ContestPost, ContestPutUsers
from View.ContestView import ContestView
from Model.ContestModel import ContestModel
from Interfase import Controller
from Classes.BuilderFile.ReportXlsx import ReportBuilder
from Classes.BuilderFile.FileOutput import FileDocx, FileXlsx, FilePDF
from Classes.Models.TypeNotify import TypeNotify
import eel


class ContestController(Controller):
    def __init__(self, model: ContestModel = ContestModel()):
        self.__model = model
        self.__view: ContestView = ContestView(self, self.__model)
        self.__proxy_contest: ContestProxy = ContestProxy()
        self.__proxy_task: TaskProxy = TaskProxy()

    def show_view(self):
        self.__model.mode_update = False
        self.__view.show_view()

    def show_view_form(self):
        self.__view.show_view_form()

    def show_view_form_update(self, id_contest: int):
        self.__model.mode_update = True
        self.__model.id_contest = id_contest
        self.__view.show_view_form()

    def load_form_contest(self):
        request = self.__proxy_contest.get_contest(self.__model.id_contest)
        self.__view.update(TypeNotify.CONTEST_FORM, contest=request)

    def add_contest(self, contest: dict):
        response = self.__proxy_contest.post_contest(contest)
        self.__model.massage = "Запись успешно добавлена"
        self.show_view()

    def delete_contest(self, id_contest: int):
        response = self.__proxy_contest.delete_contest(id_contest)
        self.load_contests()

    def update_contest(self, contest: dict):

        response = self.__proxy_contest.update_contest(contest)
        self.__model.massage = "Запись успешно изменена"
        self.show_view()

    def load_contests(self):
        request = self.__proxy_contest.get_list_contest()
        self.__view.update(TypeNotify.CONTEST_TABLE, contests=request)

    def registration_users_contest(self, users):
        data = {
            "id": self.__model.id_contest,
            "users": users
        }
        contest_users = ContestPutUsers(**data)
        response = self.__proxy_contest.registration_users_contest(contest_users)
        self.__model.massage = "участники успешно добавлены"
        self.load_contests()

    def create_report(self, id_contest: int, type_contest:int,  settings_report: dict):
        response = self.__proxy_contest.get_report_total(id_contest)
        if settings_report["typeReport"] == "Exel":
            file = FileXlsx()
        elif settings_report["typeReport"] == "Word":
            file = FileDocx()
        else:
            file = FilePDF()
        file = ReportBuilder(response, type_contest, file)
        file.build_name_column()
        file.build_main_body()
        file.file.return_file(f"{settings_report['pathFile']}/{settings_report['nameFile']}")

    def load_user_in_contest(self, id_contest: int) -> List[dict]:
        self.__model.id_contest = id_contest
        user_proxy = UserProxy()
        if id_contest != -1:
            users = user_proxy.get_in_contest_users(id_contest)
            return users

    def load_team_in_contest(self, id_contest: int) -> List[dict]:
        self.__model.id_contest = id_contest
        team_proxy = TeamProxy()
        if id_contest != -1:
            teams = team_proxy.get_list_team_in_contest(id_contest)
            return teams

    def get_mode_update(self) -> int:
        return self.__model.mode_update

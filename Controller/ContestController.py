from typing import List
from Classes.ProxyController import ContestProxy, TaskProxy, UserProxy, TeamProxy

from Classes.Models.Contest import ContestGet, ContestPost, ContestPutUsers
from Classes.Models.Task import TaskPutInServer, TaskPostInServer
from View.ContestView import ContestView
from Model.ContestModel import ContestModel
from Interfase import Controller
from Classes.BuilderFile.ReportXlsx import ReportBuilder
from Classes.BuilderFile.FileOutput import FileDocx, FileXlsx, FilePDF
import eel


class ContestController(Controller):
    def __init__(self, model: ContestModel = ContestModel(),
                 proxy_contest: ContestProxy = ContestProxy(),
                 proxy_task: TaskProxy = TaskProxy()):
        self.__model = model
        self.__view: ContestView = ContestView(self, self.__model)
        self.__proxy_contest = proxy_contest
        self.__proxy_task = proxy_task

    def show_view(self):
        self.__view.show_view()

    def add_contest(self):
        contest = self.__model.json_select_contest()
        contest.pop("id")
        response = self.__proxy_contest.post_contest(contest)
        self.__model.add_contest(response)
        self.__model.massage = "Запись успешно добавлена"

    def delete_contest(self):
        contest = self.__model.select_contest
        response = self.__proxy_contest.delete_contest(contest.id)
        self.__model.delete_contest(response)

    def update_contest(self):
        contest = self.__model.json_select_contest()
        response = self.__proxy_contest.update_contest(contest)
        self.__model.update_contest(response)
        self.__model.massage = "Запись успешно изменена"

    def load_contests(self):
        self.__model.contests = self.__proxy_contest.get_list_contest()

    def registration_users_contest(self):
        contest = self.__model.select_contest
        data = {
            "id": contest.id,
            "users": contest.users
        }
        contest_users = ContestPutUsers(**data)
        response = self.__proxy_contest.registration_users_contest(contest_users)
        self.__model.update_contest(response)
        self.__model.massage = "участники успешно добавлены"

    def add_task(self):
        task = self.__model.select_task.dict()
        task.pop("id")
        task["file"] = open(self.__model.select_task.path_test_file, "rb").read().decode("utf-8")
        response = self.__proxy_task.post_task(TaskPostInServer(**task))
        self.__model.add_task(response)
        self.__model.massage = "Запись успешно добавлена"

    def delete_task(self):
        task = self.__model.select_task
        response = self.__proxy_task.delete_task(task.id)
        self.__model.delete_task(response)
        self.__model.massage = "Запись успешно удалена"

    def update_task(self):
        task = self.__model.select_task.dict()
        try:
            task["file"] = open(task["path_test_file"], "rb").read().decode("utf-8")
        except Exception:
            task["file"] = b"".decode("utf-8")
        response = self.__proxy_task.put_task(TaskPutInServer(**task))
        self.__model.update_task(response)
        self.__model.massage = "Запись успешно изменена"

    def load_tasks(self):
        self.__model.tasks()

    def create_report(self, settings_report: dict):
        contest = self.__model.select_contest
        response = self.__proxy_contest.get_report_total(contest.id)
        if settings_report["typeReport"] == "Exel":
            file = FileXlsx()
        elif settings_report["typeReport"] == "Word":
            file = FileDocx()
        else:
            file = FilePDF()
        file = ReportBuilder(response, contest.type.value, file)
        file.build_name_column()
        file.build_main_body()
        file.file.return_file(f"{settings_report['pathFile']}/{settings_report['nameFile']}")

    def load_user_in_contest(self, id_contest: int) -> List[dict]:
        user_proxy = UserProxy()
        if id_contest != -1:
            users = user_proxy.get_in_contest_users(id_contest)
            return users

    def load_team_in_contest(self, id_contest: int) -> List[dict]:
        team_proxy = TeamProxy()
        if id_contest != -1:
            teams = team_proxy.get_list_team_in_contest(id_contest)
            return teams

    def set_select_task(self, task: dict):
        self.__model.select_task = task

    def set_select_contest(self, contest: dict):
        self.__model.select_contest = contest

    def update_select_contest(self, contest: dict):
        self.__model.update_select_contest(contest)

    def update_select_task(self, task: dict):
        self.__model.update_select_task(task)

    def clear_select_contest(self):
        self.__model.clear_select_contest()

    def clear_select_task(self):
        self.__model.clear_select_task()
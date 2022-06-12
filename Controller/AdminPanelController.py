import requests
from View.AdminPanelView import AdminPanelView
from Classes.ProxyController.AdminPanelProxy import AdminPanelProxy
from Controller.Tabs.TabContest import TabContest
from Controller.Tabs.TabTask import TabTask
from Controller.Tabs.TabTeam import TabTeam
from Controller.Tabs.TabUser import TabUser
from pykson import Pykson
from Classes.EelModification import EelModification
from Classes.Models.Team import ContestTeam


class AdminPanelController:
    def __init__(self, model):
        self.__model = model
        self.__proxy = AdminPanelProxy()
        self.__view = AdminPanelView(self, self.__model)
        self.__tab_contest = TabContest(self.__model, self.__proxy)
        self.__tab_task = TabTask(self.__model, self.__proxy)
        self.__tab_team = TabTeam(self.__model, self.__proxy)
        self.__tab_user = TabUser(self.__model, self.__proxy)

    def show_view(self):
        self.__view.show_view()

    def default(self):
        pass

    def close_window(self):
        EelModification.close_window(self.__view.name_window)

    def add_user(self):
        self.__model.add_user(self.__model.select_user)
        response = self.__tab_user.add_user()
        self.__model.massage = response[1]

    def update_user(self):
        self.__model.update_user(self.__model.select_user)
        response = self.__tab_user.update_user()
        self.__model.massage = response[1]

    def delete_user(self):
        self.__model.delete_user(self.__model.select_user)
        response = self.__tab_user.delete_user()
        self.__model.massage = response[1]

    def load_users(self):
        is_send, response = self.__tab_user.load_users()
        if is_send:
            self.__model.users = response[1]["users"]

    def add_contest(self):
        self.__model.add_contest(self.__model.contest_select)
        response = self.__tab_contest.add_contest()
        self.__model.massage = response[1]

    def delete_contest(self):
        self.__model.delete_contest(self.__model.contest_select)
        response = self.__tab_contest.delete_contest()
        self.__model.massage = response[1]

    def update_contest(self):
        self.__model.update_contest(self.__model.contest_select)
        response = self.__tab_contest.update_contest()
        self.__model.massage = response[1]

    def load_contest(self, mode):
        is_send, response = self.__tab_contest.load_contests(mode)
        if is_send:
            self.__model.contests = response[1]["contests"]

    def add_task(self):
        is_send, response = self.__tab_task.add_task()
        self.__model.massage = response["massage"]
        select_task = self.__model.select_task
        select_task.id = response["task"]["id"]
        self.__model.add_task(select_task)

    def delete_task(self):
        self.__model.delete_task(self.__model.select_task)
        response = self.__tab_task.delete_task()
        self.__model.massage = response[1]

    def update_task(self):
        self.__model.update_task(self.__model.select_task)
        response = self.__tab_task.update_task()
        self.__model.massage = response[1]

    def load_task(self):
        """"refactor"""
        id_contest = self.__model.contest_select.id
        contest = list(filter(lambda x: x["id"] == id_contest, self.__model.contests))
        self.__model.tasks = contest[0]["tasks"]

    def update_team(self):
        self.__model.update_team(self.__model.select_team)
        response = self.__tab_team.update_team()
        self.__model.massage = response[1]
        self.load_users()

    def delete_team(self):
        self.__model.delete_team(self.__model.select_team)
        response = self.__tab_team.delete_team()
        self.__model.massage = response[1]
        self.load_users()

    def add_team(self):
        is_send, response = self.__tab_team.add_teams()
        self.__model.massage = response["massage"]
        select_team = self.__model.select_team
        select_team.id = response["team"]["id"]
        contest = list(filter(lambda x: x["id"] == select_team.id_contest, self.__model.contests))[0]
        select_team.contest = Pykson().from_json(contest, ContestTeam, accept_unknown=True)
        self.__model.add_team(select_team)
        self.load_users()

    def load_team(self):
        is_send, response = self.__tab_team.load_team()
        if is_send:
            self.__model.teams = response[1]["teams"]

    def registration_user_event(self, data):
        self.__tab_team.registration_user_event(data)
        self.__model.add_team(self.__model.select_team)
        self.load_users()

    def set_select_user(self, user):
        self.__model.select_user = user

    def set_select_contest(self, contest):
        self.__model.contest_select = contest

    def set_select_task(self, task):
        self.__model.select_task = task

    def set_select_team(self, team):
        self.__model.select_team = team

    def create_report(self):
        self.__tab_contest.create_report()


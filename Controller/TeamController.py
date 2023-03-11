from Classes.ProxyController import TeamProxy, UserProxy
from typing import List
from Classes.Models.Team import TeamGet, TeamPost
from View.TeamView import TeamView
from Model.TeamModel import TeamModel
from Interfase import Controller
from Classes.Models.TypeNotify import TypeNotify
import eel


class TeamController(Controller):
    def __init__(self, model: TeamModel = TeamModel()):
        self.__model = model
        self.__view: TeamView = TeamView(self, self.__model)
        self.__proxy: TeamProxy = TeamProxy()

    def show_view(self):
        self.__view.show_view()

    def show_view_form(self):
        self.__model.mode_update = False
        self.__view.show_view_form()

    def show_view_form_update(self, id_team: int):
        self.__model.mode_update = True
        self.__model.id_team = id_team
        self.__view.show_view_form()

    def load_form_team(self):
        request = self.__proxy.get_one_team(self.__model.id_team)
        self.__view.update(TypeNotify.TEAM_FORM, team=request)

    def add_team(self, team: dict):
        request = self.__proxy.post_team(TeamPost(**team))
        self.show_view()

    def delete_team(self, id_team: int):
        request = self.__proxy.delete_team(id_team)
        self.load_team()

    def update_team(self, team: dict):
        request = self.__proxy.put_team(TeamGet(**team))
        self.show_view()

    def load_team(self):
        teams = self.__proxy.get_team()
        self.__view.update(TypeNotify.TEAM_TABLE, teams=teams)

    def load_user_in_team(self, id_team: int) -> List[dict]:
        proxy_user = UserProxy()
        if id_team is None:
            return proxy_user.get_users(params={"type_user": "user"})
        return proxy_user.get_in_team_users(id_team)

    def get_mode_update(self) -> int:
        return self.__model.mode_update



from Classes.ProxyController import TeamProxy, UserProxy
from typing import List
from Classes.Models.Team import TeamGet, TeamPost
from View.TeamView import TeamView
from Model.TeamModel import TeamModel
from Interfase import Controller
import eel


class TeamController(Controller):
    def __init__(self, model: TeamModel = TeamModel()):
        self.__model = model
        self.__view: TeamView = TeamView(self, self.__model)
        self.__proxy: TeamProxy = TeamProxy()

    def show_view(self):
        self.__view.show_view()

    def add_team(self):
        self.__model.update_select_team({"is_solo": False})
        team = self.__model.select_team.dict()
        team.pop("id")
        request = self.__proxy.post_team(TeamPost(**team))
        self.__model.add_team(request)

    def delete_team(self):
        team = self.__model.select_team
        request = self.__proxy.delete_team(team.id)
        self.__model.delete_team(request)

    def update_team(self):
        team = self.__model.select_team
        request = self.__proxy.put_team(team)
        self.__model.update_team(request)

    def load_team(self):
        self.__model.teams = self.__proxy.get_team()

    def load_user_in_team(self, id_team: int) -> List[dict]:
        proxy_user = UserProxy()
        return proxy_user.get_in_team_users(id_team)

    def update_select_team(self, data: dict):
        self.__model.update_select_team(data)

    def set_select_team(self, data: dict):
        self.__model.select_team = data

    def clear_select_team(self):
        self.__model.clear_select_team()

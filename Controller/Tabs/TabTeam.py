from json import loads, dumps
import requests
import eel
from pykson import Pykson
from Classes.Models.Team import Team
from Classes.Models.UserToTeam import UserToTeam
from Classes.Models.TeamToUser import TeamToUser


class TabTeam:
    def __init__(self, model, proxy):
        self.__model = model
        self.__admin_panel_proxy = proxy

    def add_teams(self):
        team = Pykson().to_dict_or_list(self.__model.select_team)
        return self.__admin_panel_proxy.add_team({"team": dumps(team)})

    def registration_user_event(self, data):
        user = self.__model.select_user
        team = Team()
        team.name_team = f"{user.sename} {user.name[0]}. {user.secondname[0]}."
        team.id_contest = data["id_contest"]
        team.state_contest = 1
        team.is_solo = True

        team_to_user = Pykson().from_json(Pykson().to_dict_or_list(team), TeamToUser, accept_unknown=True)

        user.team = team_to_user
        self.__model.update_user(user)

        user = Pykson().to_dict_or_list(user)

        team.users.append(Pykson().from_json(user, UserToTeam, accept_unknown=True))
        self.__model.select_team = Pykson().to_dict_or_list(team)
        self.add_teams()

    def delete_team(self):
        team = Pykson().to_dict_or_list(self.__model.select_team)
        return self.__admin_panel_proxy.delete_team(team)

    def update_team(self):
        team = Pykson().to_dict_or_list(self.__model.select_team)
        return self.__admin_panel_proxy.update_team({"team": dumps(team)})

    def load_team(self):
        data = {"id": 0}
        return self.__admin_panel_proxy.load_to_database_team(data)
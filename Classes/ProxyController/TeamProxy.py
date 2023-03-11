from Interfase.Proxy.Team import Team
from Classes.ProxyController.TeamAPI import TeamAPI
from ..Models.Team import TeamGet, TeamPost
from functools import partial


class TeamProxy(Team):
    def __init__(self):
        self.__api: TeamAPI = TeamAPI()
        self.operations = []

    def get_team(self):
        func = partial(self.__api.get_team)
        self.operations.append(func)
        return func()

    def get_one_team(self, id_team: int):
        func = partial(self.__api.get_one_team, id_team)
        self.operations.append(func)
        return func()

    def post_team(self, team: TeamPost):
        func = partial(self.__api.post_team, team)
        self.operations.append(func)
        return func()

    def put_team(self, team: TeamGet):
        func = partial(self.__api.put_team, team)
        self.operations.append(func)
        return func()

    def delete_team(self, id_team: int):
        func = partial(self.__api.delete_team, id_team)
        self.operations.append(func)
        return func()

    def get_list_team_in_contest(self, id_contest: int):
        func = partial(self.__api.get_list_team_in_contest, id_contest)
        self.operations.append(func)
        return func()

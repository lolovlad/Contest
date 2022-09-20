from typing import List
from Interfase.Proxy.Team import Team
from Classes.RequestsAPI import RequestsAPI
from Classes.Models.Team import TeamGet, TeamPost


class TeamAPI(Team):
    def __init__(self, api: RequestsAPI = RequestsAPI()):
        self.__api = api

    def get_team(self) -> List[dict]:
        return self.__api.get("teams", {})

    def post_team(self, team: TeamPost) -> dict:
        return self.__api.post("teams", team.dict())

    def put_team(self, team: TeamGet) -> dict:
        return self.__api.put("teams", team.dict())

    def delete_team(self, id_team: int) -> dict:
        return self.__api.delete(f"teams/{id_team}", {})

    def get_list_team_in_contest(self, id_contest: int) -> dict:
        return self.__api.get(f"teams/in_contest/{id_contest}", {})


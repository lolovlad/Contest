from typing import List

from Classes.Session import Session
from Interfase.Proxy.Team import Team
from Classes.RequestsAPI import RequestsAPI
from Classes.Models.Team import TeamGet, TeamPost


class TeamAPI(Team):
    def __init__(self):
        self.__api: RequestsAPI = RequestsAPI(Session().token.access_token)

    def get_team(self) -> List[dict]:
        return self.__api.get("teams", {})

    def get_one_team(self, id_team: int) -> dict:
        return self.__api.get(f"teams/{id_team}", {})

    def post_team(self, team: TeamPost) -> dict:
        return self.__api.post_token("teams", team.dict())

    def put_team(self, team: TeamGet) -> dict:
        return self.__api.put_token("teams", team.dict())

    def delete_team(self, id_team: int) -> dict:
        return self.__api.delete_toke(f"teams/{id_team}", {})

    def get_list_team_in_contest(self, id_contest: int) -> dict:
        return self.__api.get(f"teams/in_contest/{id_contest}", {})


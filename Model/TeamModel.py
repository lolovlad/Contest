from typing import List

from Interfase import Subject, Observer
from Classes.Models.TypeNotify import TypeNotify
from Classes.Models.Team import TeamGet


class TeamModel(Subject):
    def __init__(self):
        self.__observer: List[Observer] = []
        self.__select_team: TeamGet = TeamGet()
        self.__teams: List[TeamGet] = []

    @property
    def teams(self) -> List[TeamGet]:
        return self.__teams

    @teams.setter
    def teams(self, val: List[dict]):
        self.__teams.clear()
        for team in val:
            self.__teams.append(TeamGet(**team))
        self.notify(TypeNotify.TEAM_TABLE)

    @property
    def select_team(self) -> TeamGet:
        return self.__select_team

    @select_team.setter
    def select_team(self, val: dict):
        self.__select_team = list(filter(lambda x: x.id == val["id"], self.__teams))[0]
        self.notify(TypeNotify.TEAM_FORM)

    def clear_select_team(self):
        self.__select_team = TeamGet()

    def update_select_team(self, team: dict):
        try:
            team_dict = self.__select_team.dict()
            for key in team:
                team_dict[key] = team[key]
            self.__select_team = TeamGet(**team_dict)
            print(self.__select_team)
        except ValueError as e:
            #eel.errorUpdateFieldUser(e)
            pass

    def add_team(self, team: dict):
        self.__teams.append(TeamGet(**team))
        self.notify(TypeNotify.TEAM_TABLE)

    def delete_team(self, team: dict):
        for i, _team in enumerate(self.__teams):
            if _team.id == team["id"]:
                self.__teams.pop(i)
                break
        self.notify(TypeNotify.TEAM_TABLE)

    def update_team(self, team: dict):
        for i, _team in enumerate(self.__teams):
            if _team.id == team["id"]:
                self.__teams[i] = TeamGet(**team)
                break
        self.notify(TypeNotify.TEAM_TABLE)

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify: TypeNotify):
        for observer in self.__observer:
            observer.update(type_notify)

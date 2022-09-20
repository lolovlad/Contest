import eel
from Interfase.View import View
from Model.TeamModel import TeamModel
from Classes.Models.TypeNotify import TypeNotify


class TeamView(View):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model: TeamModel = model
        self.__model.attach(self)
        self.__file_templates: str = "templates/team.html"

    def show_view(self):
        eel.locationReplace(self.__file_templates)

    def update(self, type_notify: TypeNotify):
        if type_notify == TypeNotify.TEAM_TABLE:
            teams = [user.dict() for user in self.__model.teams]
            eel.updateTeamTabel(teams)
        elif type_notify == TypeNotify.TEAM_FORM:
            eel.loadFormTeam(self.__model.select_team.dict())
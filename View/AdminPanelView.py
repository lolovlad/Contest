import eel
from random import randint
from Interfase.Observer import Observer
from Interfase.View import View
from pykson import Pykson


class AdminPanelView(Observer, View):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.attach(self)
        self.__file_templates = 'admin_panel.html'
        self.__port = randint(8000, 8030)
        self.__geometry = {'size': (760, 760), 'position': ()}
        self.__name_window = "AdminPanel"

    @property
    def name_window(self):
        return self.__name_window

    def show_view(self):
        self._full_screen(self.__geometry)
        self._create_geometry(self.__geometry)
        eel.start(self.__file_templates, mode="chrome", size=self.__geometry["size"],
                  port=self.__port, position=self.__geometry["position"])

    def update(self, type_notify):
        if type_notify == "tab_user":
            eel.updateUserTable(self.__model.users)
            new_users = list(filter(lambda x: x["type"] != 1 and x["team"] is None, self.__model.users))
            eel.updateUserTableModel(new_users)
        if type_notify == "massage":
            eel.alert(self.__model.massage)
        if type_notify == "tab_contest":
            eel.loadSelectContest(self.__model.contests)
            eel.updateContestTable(self.__model.contests)
        if type_notify == "tab_task":
            eel.updateTaskTable(self.__model.tasks)
        if type_notify == "tab_task_to_form":
            eel.loadFormTask(Pykson().to_dict_or_list(self.__model.select_task))
        if type_notify == "tab_team_to_form":
            eel.loadFormTeam(Pykson().to_dict_or_list(self.__model.select_team))
            new_users = list(filter(lambda x: x["type"] != 1 and x["team"] is None, self.__model.users))
            eel.updateUserTableModel(new_users)
        if type_notify == "tab_team":
            eel.updateTeamTabel(self.__model.teams)

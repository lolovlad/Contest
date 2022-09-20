import eel
from Interfase.Observer import Observer
from random import randint
from Interfase.View import View
from json import loads


class MainWindowView(Observer, View):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.attach(self)
        self.__file_templates: str = 'main.html'
        self.__geometry: dict = {'size': (720, 760), 'position': (300, 50)}
        self.__name_window: str = "Main"
        self.__port: int = randint(8000, 8030)

    @property
    def name_window(self):
        return self.__name_window

    def show_view(self):
        eel.locationReplace(self.__file_templates)

    def update(self, type_notify=None):
        if type_notify == "contests":
            eel.loadsLeftInformation(self.__model.contest)
        if type_notify == "select_task":
            new_tasks = self.__model.select_task
            files = self.__model.files
            new_tasks["path_test_file"] = files[new_tasks["path_test_file"]]
            eel.loadSelectTask(new_tasks)
        if type_notify == "tasks_update":
            new_tasks = self.__model.tasks
            files = self.__model.files
            for task in new_tasks:
                task["path_test_file"] = files[task["path_test_file"]]
            eel.loadsTasks(new_tasks)
        if type_notify == "select_answers":
            eel.loadAnswers(self.__model.answers)
        if type_notify == "menu":
            eel.loadMenu(self.__model.menu)
        if type_notify == "close_contest":
            eel.closeContest()
        if type_notify == "select_report":
            eel.loadsReports(self.__model.select_report)

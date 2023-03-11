import eel
from Interfase.View import View
from Model.ContestModel import ContestModel
from Classes.Models.TypeNotify import TypeNotify


class ContestView(View):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model: ContestModel = model
        self.__model.attach(self)
        self.__file_templates: str = "templates/contest.html"

    def show_view(self):
        eel.locationReplace(self.__file_templates)

    def show_view_form(self):
        eel.locationReplace("templates/contest_form.html")

    def update(self, type_notify: TypeNotify, **kwargs):
        if type_notify == TypeNotify.CONTEST_TABLE:
            eel.updateContestTable(kwargs["contests"])
        elif type_notify == TypeNotify.CONTEST_FORM:
            eel.loadFormContest(kwargs["contest"])
        elif type_notify == TypeNotify.TASK_TABLE:
            tasks = [task.dict() for task in self.__model.select_contest.tasks]
            eel.updateTaskTable(tasks)
        elif type_notify == TypeNotify.TASK_FORM:
            eel.loadFormTask(self.__model.select_task.dict())
import eel
from Interfase.Observer import Observer
from random import randint
from Interfase.View import View


class PackageView(Observer, View):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__file_templates = 'posl.html'
        self.__name_window = "Package"
        self.__geometry = {'size': (720, 760), 'position': (300, 50)}
        self.__port = randint(8000, 8030)

    @property
    def name_window(self):
        return self.__name_window

    def show_view(self):
        eel.start(self.__file_templates, mode="chrome",
                  size=self.__geometry["size"], port=self.__port, position=self.__geometry["position"])

    def update(self, type_notify=None):
        if type_notify == "answers":
            eel.loadsAnswersPackage(self.__model.answers)
        if type_notify == "select_report":
            eel.loadsReportsPackage(self.__model.select_report)
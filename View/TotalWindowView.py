import eel
from Interfase.Observer import Observer
from Interfase.View import View
from random import randint
from Classes.EelModification import EelModification


class TotalWindowView(Observer, View):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.attach(self)
        self.__file_templates = 'total.html'
        self.__name_window = "Total"
        self.__port = randint(8000, 8030)
        self.__geometry = {'size': (760, 760), 'position': (300, 50)}
        self._create_geometry(self.__geometry)

    @property
    def name_window(self):
        return self.__name_window

    def show_view(self):
        eel.start(self.__file_templates, mode="chrome", size=self.__geometry["size"],
                  port=self.__port, position=self.__geometry["position"])

    def update(self, type_notify=None):
        if type_notify == "report_contest":
            eel.loadTotalContest(self.__model.total_report)
        if type_notify == "contests":
            eel.loadContest(self.__model.contests)
        if type_notify == "select_contest":
            self.__controller.load_total_report()

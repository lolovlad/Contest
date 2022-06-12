import eel
from random import randint
from Interfase.Observer import Observer
from Interfase.View import View


class MenuView(Observer, View):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.attach(self)
        self.__file_templates = 'menu.html'
        self.__name_window = "Menu"
        self.__port = randint(8000, 8030)
        self.__geometry = {'size': (720, 760), 'position': (300, 50)}

    @property
    def name_window(self):
        return self.__name_window

    def show_view(self):
        self._full_screen(self.__geometry)
        self._create_geometry(self.__geometry)
        eel.start(self.__file_templates, mode="chrome",
                  size=self.__geometry["size"], port=self.__port, position=self.__geometry["position"])

    def update(self, type_notify=None):
        if type_notify == "contests":
            eel.updateMenuContest(self.__model.contests)
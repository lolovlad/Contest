import eel
from random import randint
from Interfase.Observer import Observer
from Interfase.View import View
from random import randint


class LoginView(Observer, View):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.attach(self)
        self.__file_templates = 'login.html'
        self.__geometry = {'size': (720, 760), 'position': (300, 50)}
        self.__name_window = "Login"
        self.__port = randint(8000, 8030)

    @property
    def name_window(self):
        return self.__name_window

    def show_view(self):
        self._create_geometry(self.__geometry)
        try:
            eel.start(self.__file_templates, mode="chrome",
                      size=self.__geometry["size"], port=self.__port, position=self.__geometry["position"])
        except OSError:
            self.__port = randint(8000, 8030)
            eel.start(self.__file_templates, mode="chrome",
                      size=self.__geometry["size"], port=self.__port, position=self.__geometry["position"])

    def update(self, type_notify=None):
        eel.update_error(self.__model.error)


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
        self.__name_window = "Login"
        self.__port = randint(8000, 8030)

    @property
    def name_window(self):
        return self.__name_window

    def show_view(self):
        eel.show(self.__file_templates)

    def update(self, type_notify=None):
        eel.update_error(self.__model.error)


import eel
from random import randint
from Interfase.Observer import Observer
from Interfase.View import View

from Model.MenuModel import MenuModel


class MenuView(Observer, View):
    def __init__(self, controller, model: MenuModel):
        self.__controller = controller
        self.__model: MenuModel = model
        self.__model.attach(self)
        self.__file_templates: str = 'menu.html'
        self.__name_window: str = "Menu"
        self.__port: int = randint(8000, 8030)
        self.__geometry: dict = {'size': (720, 760), 'position': (300, 50)}

    def show_view(self):
        eel.locationReplace(self.__file_templates)

    def update(self, type_notify=None):
        if type_notify == "contests":
            eel.updateMenuContest(self.__model.contests)
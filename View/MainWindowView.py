import eel
from Interfase.Observer import Observer


class MainWindowView(Observer):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.attach(self)

    def show_view(self, id_contest):
        self.__model.id_contest = id_contest
        eel.start('main.html', mode="chrome", size=(760, 760), port=2000)

    def update(self):
        self.__controller.load_contest()
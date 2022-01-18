import eel
from Interfase.Observer import Observer


class MainWindowView(Observer):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.attach(self)

    def show_view(self):
        eel.start('main.html', mode="chrome", size=(760, 760), port=2000)

    def update(self):
        pass
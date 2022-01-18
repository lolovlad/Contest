import eel
from Interfase.Observer import Observer


class LoginView(Observer):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.attach(self)

    def show_view(self):
        eel.start('login.html', mode="chrome", size=(760, 760))

    def update(self):
        eel.update_error(self.__model.error)


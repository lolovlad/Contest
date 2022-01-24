import eel
from Interfase.Observer import Observer


class AdminPanelView(Observer):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model = model
        self.__model.attach(self)

    def show_view(self):
        eel.start('admin_panel.html', mode="chrome", size=(760, 760), port=3000)

    def update(self):
        pass
        #eel.update_error(self.__model.error)
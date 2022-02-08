import requests

from View.MenuView import MenuView
import eel


class MenuController:
    def __init__(self, model):
        self.__model = model
        self.__view = MenuView(self, self.__model)

    def show_view(self):
        self.__view.show_view()

    def default(self):
        pass

    def load_contest(self):
        BASE = "http://127.0.0.1:5000"
        response = requests.get(f"{BASE}/contests/1")
        response = response.json()
        eel.updateMenuContest(response)


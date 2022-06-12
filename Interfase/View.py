from abc import abstractmethod, ABC
from tkinter import *
from random import randint
import eel


class View(ABC):
    @abstractmethod
    def __init__(self, controller, model):
        pass

    @abstractmethod
    def show_view(self, *args):
        pass

    def __get_size_screen(self):
        tk = Tk()
        return tk.winfo_screenwidth(), tk.winfo_screenheight()

    def _create_geometry(self, geometry):
        weight, height = self.__get_size_screen()
        size_weight, size_height = geometry["size"]
        geometry["position"] = ((weight // 2) - (size_weight // 2), (height // 2) - (size_height // 2))

    def _full_screen(self, geometry):
        geometry["size"] = self.__get_size_screen()


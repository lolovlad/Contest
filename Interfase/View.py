from abc import abstractmethod, ABC
from tkinter import *


class View(ABC):
    @abstractmethod
    def __init__(self, controller, model):
        pass

    @abstractmethod
    def show_view(self, *args):
        pass


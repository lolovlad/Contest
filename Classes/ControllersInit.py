from Interfase.Singleton import Singleton

from Controller.LoginController import LoginController
from Controller.MainWindowController import MainWindowController
from Controller.MenuController import MenuController
from Controller.PackageController import PackageController
from Controller.TotalWindowController import TotalWindowController
from Controller import UserController, TeamController, ContestController
from Classes.TaskPage import TaskPage


class ControllersInit(metaclass=Singleton):
    def __init__(self):
        self.login: LoginController = LoginController(self)
        self.user: UserController = None
        self.team: TeamController = None
        self.contest: ContestController = None
        self.main_window = None
        self.menu = None
        self.package = None
        self.total = None
        self.task: TaskPage = None
        self.__target = self.login

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, val):
        self.__target = val

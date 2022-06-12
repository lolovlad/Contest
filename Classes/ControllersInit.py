from Interfase.Singleton import Singleton

from Controller.AdminPanelController import AdminPanelController
from Controller.LoginController import LoginController
from Controller.MainWindowController import MainWindowController
from Controller.MenuController import MenuController
from Controller.PackageController import PackageController
from Controller.TotalWindowController import TotalWindowController

from Model.AdminPanelModel import AdminPanelModel
from Model.LoginModel import LoginModel
from Model.MainWindowModel import MainWindowModel
from Model.MenuModel import MenuModel
from Model.PackageModel import PackageModel
from Model.TotalWindowModel import TotalWindowModel


class ControllersInit(metaclass=Singleton):
    def __init__(self):
        self.login = LoginController(LoginModel(), self)
        self.admin_panel = AdminPanelController(AdminPanelModel())
        self.main_window = MainWindowController(MainWindowModel())
        self.menu = MenuController(MenuModel())
        self.package = PackageController(PackageModel())
        self.total = TotalWindowController(TotalWindowModel())
        self.__target = self.login

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, val):
        self.__target = val

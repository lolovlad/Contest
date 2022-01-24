from Interfase.Singleton import Singleton

from Controller.AdminPanelController import AdminPanelController
from Controller.LoginController import LoginController
from Controller.MainWindowController import MainWindowController
from Controller.MenuController import MenuController

from Model.AdminPanelModel import AdminPanelModel
from Model.LoginModel import LoginModel
from Model.MainWindowModel import MainWindowModel
from Model.MenuModel import MenuModel


class ControllersInit(metaclass=Singleton):
    def __init__(self):
        self.login = LoginController(LoginModel(), self)
        self.admin_panel = AdminPanelController(AdminPanelModel())
        self.main_window = MainWindowController(MainWindowModel())
        self.menu = MenuController(MenuModel())
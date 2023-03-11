import requests.exceptions

from Classes.ProxyController.LoginProxy import LoginProxy
from View.LoginView import LoginView
from Model.LoginModel import LoginModel
from Classes.Session import Session
from Interfase import Controller


from Controller.UserController import UserController
from Controller.MenuController import MenuController

from Classes.Models.User import TypeUser


class LoginController(Controller):
    def __init__(self, controllers, model: LoginModel = LoginModel(),
                 login_proxy: LoginProxy = LoginProxy()):
        self.__model = model
        self.__view = LoginView(self, self.__model)
        self.__controllers = controllers
        self.__login_proxy = login_proxy

    def show_view(self):
        self.__view.show_view()

    def login(self):
        self.__login_proxy.login(self.__model.login.dict())
        try:
            response: dict = self.__login_proxy.send()
        except requests.exceptions.ConnectionError:
            response = {"message": "Не удалось установить соединение с сервером"}
        if response.get("message") is None:
            self.__model.token = response
            if Session().token.type_user == TypeUser.ADMIN:
                self.__controllers.user = UserController()
                self.__controllers.user.show_view()
            elif Session().token.type_user == TypeUser.USER:
                self.__controllers.menu = MenuController()
                self.__controllers.menu.show_view()
        else:
            self.__model.error = response["message"]

    def set_login(self, login: dict):
        self.__model.login = login



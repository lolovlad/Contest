from Classes.ProxyController.LoginProxy import LoginProxy
from View.LoginView import LoginView
from Classes.EelModification import EelModification
from Classes.Session import Session


class LoginController:
    def __init__(self, model, controllers):
        self.__model = model
        self.__view = LoginView(self, self.__model)
        self.__controllers = controllers
        self.__login_proxy = LoginProxy()

    def show_view(self):
        self.__view.show_view()

    def login(self):
        data = {"login": self.__model.login,
                "password": self.__model.password}

        self.__login_proxy.login(data)
        response = self.__login_proxy.send()[0]
        if response[0]:
            body_response = response[1]
            self.__model.user = body_response["user"]
            Session().user = self.__model.user
            if self.__model.user.type == 1:
                EelModification.close_window(self.__view.name_window)
                self.__controllers.admin_panel.show_view()
            elif self.__model.user.type == 2:
                EelModification.close_window(self.__view.name_window)
                self.__controllers.menu.show_view()
        else:
            self.__model.error = response[1]

    def set_login(self, login):
        self.__model.login = login

    def set_password(self, password):
        self.__model.password = password



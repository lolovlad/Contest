from Classes.ProxyController import UserProxy, EducationalOrganizationsProxy

from Classes.Models.User import UserUpdate, UserPost
from View.UserView import UserView
from Model.UserModel import UserModel
from Interfase import Controller
import eel


class UserController(Controller):
    def __init__(self, model: UserModel = UserModel(), proxy: UserProxy = UserProxy()):
        self.__model = model
        self.__view: UserView = UserView(self, self.__model)
        self.__proxy = proxy

    def show_view(self):
        self.__view.show_view()

    def add_user(self):
        user = self.__model.select_user.dict()
        user.pop("id")
        user = UserPost(**user)
        response = self.__proxy.post_user(user)
        self.__model.add_user(response)
        #self.__model.massage = "Запись успешно добавлена"

    def update_user(self):
        user = self.__model.select_user
        response = self.__proxy.put_user(user)
        self.__model.update_user(response)

    def delete_user(self):
        user = self.__model.select_user
        response = self.__proxy.delete_user(user.id)
        self.__model.delete_user(response)

    def load_user(self):
        response = self.__proxy.get_users()
        self.__model.users = response

    def set_select_user(self, user: dict):
        self.__model.select_user = user

    def update_select_user(self, user: dict):
        self.__model.update_select_user(user)

    def clear_select_user(self):
        self.__model.clear_select_user()

    def load_organization(self):
        proxy_edu = EducationalOrganizationsProxy()
        return proxy_edu.get_organizations()

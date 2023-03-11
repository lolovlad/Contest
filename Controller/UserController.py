from Classes.ProxyController import UserProxy, EducationalOrganizationsProxy

from Classes.Models.User import UserUpdate, UserPost
from Classes.Models.TypeNotify import TypeNotify
from View.UserView import UserView
from Model.UserModel import UserModel
from Interfase import Controller
import eel


class UserController(Controller):
    def __init__(self, model: UserModel = UserModel()):
        self.__model = model
        self.__view: UserView = UserView(self, self.__model)
        self.__proxy: UserProxy = UserProxy()

    def show_view(self):
        self.__model.mode_update = False
        self.__view.show_view()

    def show_view_form(self):
        self.__model.mode_update = False
        self.__view.show_view_form()

    def show_view_form_update(self, id_user: int):
        self.__model.mode_update = True
        self.__model.select_id_user = id_user
        self.__view.show_view_form_update()

    def add_user(self, user: dict):
        user = UserPost(**user)
        self.__proxy.post_user(user)
        self.__model.massage = "Запись успешно добавлена"
        self.__view.show_view()
        self.load_user()

    def update_user(self, user: dict):
        response = self.__proxy.put_user(UserUpdate(**user))
        self.__model.massage = "Запись успешно добавлена"
        self.__view.show_view()
        self.load_user()

    def delete_user(self, id_user: int):
        response = self.__proxy.delete_user(id_user)
        self.__model.massage = "Запись успешно добавлена"
        self.load_user()

    def load_user(self):
        response = self.__proxy.get_users(params={"type_user": "all"})
        self.__view.update(TypeNotify.USER_TABLE, users=response)

    def load_form_user(self):
        user = self.__proxy.get_user(self.__model.select_id_user)
        self.__view.update(TypeNotify.USER_FORM, user=user)

    def get_mode_update(self):
        return self.__model.mode_update

    def load_organization(self, type_edu: int):
        proxy_edu = EducationalOrganizationsProxy()
        organization = proxy_edu.get_organizations_type(type_edu)
        return organization

import eel
from Interfase.Observer import Observer
from Interfase.View import View
from Model.UserModel import UserModel
from Classes.Models.TypeNotify import TypeNotify


class UserView(View):
    def __init__(self, controller, model):
        self.__controller = controller
        self.__model: UserModel = model
        self.__model.attach(self)
        self.__file_templates: str = "templates/user.html"

    def show_view(self):
        eel.locationReplace(self.__file_templates)

    def update(self, type_notify: TypeNotify):
        if type_notify == TypeNotify.USER_TABLE:
            users = [user.dict() for user in self.__model.users]
            eel.updateUserTable(users)
        elif type_notify == TypeNotify.USER_FORM:
            eel.loadFormUser(self.__model.select_user.dict())

from Interfase.Singleton import Singleton
from Classes.Models.User import UserUpdate as User


class Session(metaclass=Singleton):
    user: User = User()

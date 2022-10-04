from Interfase.Singleton import Singleton
from Classes.Models.Login import Token


class Session(metaclass=Singleton):
    token: Token = Token()

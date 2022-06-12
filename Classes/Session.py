from Interfase.Singleton import Singleton


class Session(metaclass=Singleton):
    user = None

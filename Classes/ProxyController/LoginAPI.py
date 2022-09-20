from Interfase.Proxy.Login import Login
from Classes.RequestsAPI import RequestsAPI


class LoginAPI(Login):
    __api: RequestsAPI = RequestsAPI("123")

    def login(self, data):
        response = self.__api.get("login", data)
        return response

from Interfase.Proxy.Login import Login
from Classes.RequestsAPI import RequestsAPI


class LoginAPI(Login):
    __api = RequestsAPI("123")

    def login(self, data):
        response = self.__api.post("login", data)
        if response["message"] == "login":
            return True, response["data"]
        else:
            return False, response["data"]
from Interfase.Proxy.Login import Login
from Classes.RequestsAPI import RequestsAPI


class LoginAPI(Login):
    __api: RequestsAPI = RequestsAPI("123")

    def login(self, data: dict):
        response = self.__api.post_sign_in("login/sign-in/", data)
        return response

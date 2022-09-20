from Interfase.Proxy.Menu import Menu
from Classes.RequestsAPI import RequestsAPI
from functools import partial


class MenuAPI(Menu):

    __api = RequestsAPI()

    def load_to_database_contest(self, data):
        response = partial(self.__api.get, f"contests/contests_by_user_id/{data['id_user']}", {})
        return self.__response_api(response, "update_task")

    def __response_api(self, func, type_message) -> object:
        response = func()
        print(response)
        return response
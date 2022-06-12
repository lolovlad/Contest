from Interfase.Proxy.AdminPanel import AdminPanel
from Classes.RequestsAPI import RequestsAPI
from functools import partial


class AdminPanelAPI(AdminPanel):

    __api = RequestsAPI("123")

    def add_user(self, data):
        function_response = partial(self.__api.post, f"users/0", data)
        return self.__response_api(function_response, "add_user")

    def delete_user(self, data):
        function_response = partial(self.__api.delete, f"users/{data['id']}", data)
        return self.__response_api(function_response, "delete_user")

    def update_user(self, data):
        function_response = partial(self.__api.put, f"users/{data['id']}", data)
        return self.__response_api(function_response, "update_user")

    def load_to_database_user(self, data):
        function_response = partial(self.__api.get, f"users/0", data)
        return self.__response_api(function_response, "load_user")

    def add_contest(self, data):
        response = partial(self.__api.post, f"contests/0", data)
        return self.__response_api(response, "add_contest")

    def delete_contest(self, data):
        response = partial(self.__api.delete, f"contests/{data['id']}", data)
        return self.__response_api(response, "delete_contest")

    def update_contest(self, data):
        response = partial(self.__api.put, f"contests/{data['id']}", data)
        return self.__response_api(response, "update_contest")

    def load_to_database_contest(self, data):
        response = partial(self.__api.get, f"contests/{data['id']}", data)
        return self.__response_api(response, "load_contest")

    def add_task(self, data):
        response = partial(self.__api.post, f"tasks/0", data)
        return self.__response_api(response, "add_task")

    def delete_task(self, data):
        response = partial(self.__api.delete, f"tasks/{data['id']}", data)
        return self.__response_api(response, "delete_task")

    def update_task(self, data):
        response = partial(self.__api.put, f"tasks/0", data)
        return self.__response_api(response, "update_task")

    def load_to_database_team(self, data):
        response = partial(self.__api.get, f"teams/{data['id']}", data)
        return self.__response_api(response, "load_team")

    def add_team(self, data):
        response = partial(self.__api.post, f"teams/0", data)
        return self.__response_api(response, "add_team")

    def delete_team(self, data):
        response = partial(self.__api.delete, f"teams/{data['id']}", data)
        return self.__response_api(response, "delete_team")

    def update_team(self, data):
        response = partial(self.__api.put, f"teams/0", data)
        return self.__response_api(response, "update_team")

    def load_to_database_report_total(self, data):
        response = partial(self.__api.get, f"report_total/{data['id_contest']}", data)
        return self.__response_api(response, "load_report")

    def __response_api(self, func, type_message):
        response = func()
        if response["message"] == type_message:
            return True, response["data"]
        else:
            return False, response["data"]
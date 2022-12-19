from Interfase.Proxy.Main import Main
from Classes.RequestsAPI import RequestsAPI
from functools import partial


class MainAPI(Main):

    __api = RequestsAPI("123")

    def load_to_database_contest_page(self, data: dict):
        function_response = partial(self.__api.get, f"contests/contest_page/{data['id_contest']}", {})
        return self.__response_api(function_response, "load_json_test_file")

    def load_to_database_answers(self, data: dict):
        function_response = partial(self.__api.get,
                                    f"answers/{data['id_contest']}/{data['id_task']}/{data['id_user']}",
                                    {})
        return self.__response_api(function_response, "load_answers")

    def load_to_database_package(self, data: dict):
        function_response = partial(self.__api.get,
                                    f"answers/package/{data['id_contest']}/{data['id_user']}",
                                    {})
        return self.__response_api(function_response, "load_answers")

    def add_answer(self, data):
        function_response = partial(self.__api.post, f"answers", data)
        return self.__response_api(function_response, "add_answer")

    def update_team(self, data):
        function_response = partial(self.__api.put, f"teams/{data['id_team']}", data)
        return self.__response_api(function_response, "update_team")

    def load_to_database_json_report(self, data):
        function_response = partial(self.__api.get, f"answers/report/{data['id_answer']}", {})
        return self.__response_api(function_response, "load_report")

    def load_to_database_compilation(self, data: dict):
        function_response = partial(self.__api.get, f"type_compilation/", {})
        return self.__response_api(function_response, "load_answers")

    def get_status_user(self, data: dict):
        function_response = partial(self.__api.get, f"users/status/{data['id_contest']}/{data['id_user']}", {})
        return self.__response_api(function_response, "load_answers")

    def close_contest_to_user(self, data: dict):
        function_response = partial(self.__api.put,
                                    f"contests/close_to_user_contest/{data['id_contest']}/{data['id_user']}", {})
        return self.__response_api(function_response, "load_answers")

    def __response_api(self, func, type_message):
        response = func()
        print(response)
        return response

from Classes.Session import Session
from Interfase.Proxy.UserContestView import UserContestView
from Classes.RequestsAPI import RequestsAPI
from Classes.Models.Task import *


class UserContestViewAPI(UserContestView):
    def __init__(self):
        self.__api: RequestsAPI = RequestsAPI(Session().token.access_token)

    def get_contest(self, id_contest: int):
        return self.__api.get(f"user_contest_view/get_contest/{id_contest}", {})

    def get_list_task(self, id_contest: int):
        return self.__api.get_toke(f"user_contest_view/get_list_task/{id_contest}", {})

    def get_task(self, id_task: int):
        return self.__api.get(f"user_contest_view/get_task/{id_task}", {})

    def get_list_answers(self, id_contest: int, id_task: int):
        return self.__api.get_toke(f"user_contest_view/get_list_answers/{id_contest}/{id_task}", {})

    def get_report(self, id_answer: int):
        return self.__api.get(f"user_contest_view/get_report/{id_answer}", {})

    def close_contest(self, id_contest: int):
        return self.__api.put_token(f"user_contest_view/close_contest/{id_contest}", {})

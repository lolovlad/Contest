from typing import List
from Interfase.Proxy.Contest import Contest
from Classes.RequestsAPI import RequestsAPI
from Classes.Models.Contest import ContestPost, ContestGet, ContestPutUsers


class ContestAPI(Contest):
    def __init__(self, api: RequestsAPI = RequestsAPI()):
        self.__api = api

    def get_list_contest(self) -> List[dict]:
        return self.__api.get("contests/list_contest", {})

    def post_contest(self, contest: dict) -> dict:
        return self.__api.post("contests", contest)

    def delete_contest(self, id_contest: int) -> dict:
        return self.__api.delete(f"contests/{id_contest}", {})

    def update_contest(self, contest: dict) -> dict:
        return self.__api.put("contests", contest)

    def registration_users_contest(self, contest: ContestPutUsers) -> dict:
        return self.__api.put("contests/registration_users", contest.dict())

    def contests_by_user_id(self, id_user: int) -> List[dict]:
        return self.__api.get(f"contests/contests_by_user_id/{id_user}", {})

    def contest_page(self, id_contest: int) -> dict:
        return self.__api.get(f"contests/contest_page/{id_contest}", {})

    def close_to_user_contest(self, id_contest: int, id_user: int) -> dict:
        return self.__api.put(f"contests/close_to_user_contest/{id_contest}/{id_user}", {})

    def get_report_total(self, id_contest: int) -> List[dict]:
        return self.__api.get(f"contests/report_total/{id_contest}", {})
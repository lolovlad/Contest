from typing import List
from Interfase.Proxy.User import User
from Classes.RequestsAPI import RequestsAPI
from Classes.Models.User import UserPost, UserUpdate


class UserAPI(User):
    def __init__(self, api: RequestsAPI = RequestsAPI()):
        self.__api = api

    def get_users(self) -> List[dict]:
        return self.__api.get("users", {})

    def get_status_user(self, data: dict) -> dict:
        return self.__api.get(f"users/status/{data['id_contest']}/{data['id_user']}", {})

    def post_user(self, data: UserPost) -> dict:
        return self.__api.post(f"users", data.dict())

    def put_user(self, data: UserUpdate) -> dict:
        return self.__api.put(f"users", data.dict())

    def delete_user(self, data: int) -> dict:
        return self.__api.delete(f"users/{data}", {})

    def get_in_team_users(self, data: int) -> List[dict]:
        return self.__api.get(f"users/in_team/{data}", {})

    def get_in_contest_users(self, data: int) -> List[dict]:
        return self.__api.get(f"users/in_contest/{data}", {})
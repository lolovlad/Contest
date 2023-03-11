from typing import List
from Interfase.Proxy.User import User
from Classes.RequestsAPI import RequestsAPI
from Classes.Models.User import UserPost, UserUpdate
from Classes.Session import Session


class UserAPI(User):
    def __init__(self):
        self.__api: RequestsAPI = RequestsAPI(Session().token.access_token)

    def get_users(self, params: dict) -> List[dict]:
        return self.__api.get_toke("users", params)

    def get_user(self, id_user: int) -> dict:
        return self.__api.get_toke(f"users/{id_user}", {})

    def get_status_user(self, data: dict) -> dict:
        return self.__api.get_toke(f"users/status/{data['id_contest']}/{data['id_user']}", {})

    def post_user(self, data: UserPost) -> dict:
        return self.__api.post_token(f"users", data.dict())

    def put_user(self, data: UserUpdate) -> dict:
        return self.__api.put_token(f"users", data.dict())

    def delete_user(self, data: int) -> dict:
        return self.__api.delete_toke(f"users/{data}", {})

    def get_in_team_users(self, data: int) -> List[dict]:
        return self.__api.get(f"users/in_team/{data}", {})

    def get_in_contest_users(self, data: int) -> List[dict]:
        return self.__api.get(f"users/in_contest/{data}", {})
from typing import List

from Classes.Session import Session
from Interfase.Proxy.Task import Task
from Classes.RequestsAPI import RequestsAPI
from Classes.Models.Task import *


class TaskAPI(Task):
    def __init__(self):
        self.__api: RequestsAPI = RequestsAPI(Session().token.access_token)

    def post_task(self, task: TaskPost) -> dict:
        return self.__api.post_token("tasks", task.dict())

    def get_list_task(self, id_contest: int) -> List[dict]:
        return self.__api.get_toke(f"tasks/get_list_task/{id_contest}", {})

    def get_task(self, id_task: int) -> dict:
        return self.__api.get_toke(f"tasks/get_task/{id_task}", {})

    def put_task(self, task: TaskPut) -> dict:
        return self.__api.put_token("tasks", task.dict())

    def delete_task(self, id_task: int) -> dict:
        return self.__api.delete_toke(f"tasks/{id_task}", {})

    def put_settings_task(self, settings: TaskSettings) -> dict:
        return self.__api.put_token(f"tasks/settings/", settings.dict())

    def get_settings(self, id_task: int) -> dict:
        return self.__api.get(f"tasks/get_settings/{id_task}", {})

    def upload_files(self, id_task: int, files: dict) -> dict:
        return self.__api.post_token(f"tasks/upload_file/{id_task}", {}, files=files)

    def upload_json_files(self,  id_task: int, files: dict) -> dict:
        return self.__api.post_token(f"tasks/upload_json_files/{id_task}", {}, files=files)

    def delete_file(self, id_task: int, filename: str) -> dict:
        return self.__api.delete_toke(f"tasks/delete_file/{id_task}/{filename}", {})
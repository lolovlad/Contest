from typing import List

from Classes.Session import Session
from Interfase.Proxy.Task import Task
from Classes.RequestsAPI import RequestsAPI
from Classes.Models.Task import TaskPostInServer, TaskPutInServer


class TaskAPI(Task):
    def __init__(self):
        self.__api: RequestsAPI = RequestsAPI(Session().token.access_token)

    def post_task(self, task: TaskPostInServer) -> dict:
        return self.__api.post_token("tasks", task.dict())

    def put_task(self, task: TaskPutInServer) -> dict:
        return self.__api.put_token("tasks", task.dict())

    def delete_task(self, id_task: int) -> dict:
        return self.__api.delete_toke(f"tasks/{id_task}", {})

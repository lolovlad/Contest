from typing import List
from Interfase.Proxy.Task import Task
from Classes.RequestsAPI import RequestsAPI
from Classes.Models.Task import TaskPostInServer, TaskPutInServer


class TaskAPI(Task):
    def __init__(self, api: RequestsAPI = RequestsAPI()):
        self.__api = api

    def post_task(self, task: TaskPostInServer) -> dict:
        return self.__api.post("tasks", task.dict())

    def put_task(self, task: TaskPutInServer) -> dict:
        return self.__api.put("tasks", task.dict())

    def delete_task(self, id_task: int) -> dict:
        return self.__api.delete(f"tasks/{id_task}", {})

from Interfase.Proxy.Task import Task
from Classes.ProxyController.TaskAPI import TaskAPI
from Classes.Models.Task import TaskPostInServer, TaskPutInServer
from functools import partial


class TaskProxy(Task):
    def __init__(self, api: TaskAPI = TaskAPI()):
        self.__api = api
        self.operations = []

    def post_task(self, task: TaskPostInServer):
        func = partial(self.__api.post_task, task)
        self.operations.append(func)
        return func()

    def put_task(self, task: TaskPutInServer):
        func = partial(self.__api.put_task, task)
        self.operations.append(func)
        return func()

    def delete_task(self, id_task: int):
        func = partial(self.__api.delete_task, id_task)
        self.operations.append(func)
        return func()


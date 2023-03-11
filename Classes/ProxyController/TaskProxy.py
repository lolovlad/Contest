from Interfase.Proxy.Task import Task
from Classes.ProxyController.TaskAPI import TaskAPI
from Classes.Models.Task import TaskPost, TaskPut, TaskSettings
from functools import partial


class TaskProxy(Task):
    def __init__(self):
        self.__api: TaskAPI = TaskAPI()
        self.operations = []

    def get_list_task(self, id_contest: int):
        func = partial(self.__api.get_list_task, id_contest)
        self.operations.append(func)
        return func()

    def get_task(self, id_task: int):
        func = partial(self.__api.get_task, id_task)
        self.operations.append(func)
        return func()

    def post_task(self, task: TaskPost):
        func = partial(self.__api.post_task, task)
        self.operations.append(func)
        return func()

    def put_task(self, task: TaskPut):
        func = partial(self.__api.put_task, task)
        self.operations.append(func)
        return func()

    def delete_task(self, id_task: int):
        func = partial(self.__api.delete_task, id_task)
        self.operations.append(func)
        return func()

    def put_settings_task(self, settings: TaskSettings):
        func = partial(self.__api.put_settings_task, settings)
        self.operations.append(func)
        return func()

    def get_settings(self, id_task: int):
        func = partial(self.__api.get_settings, id_task)
        self.operations.append(func)
        return func()

    def upload_files(self, id_task: int, files: dict):
        func = partial(self.__api.upload_files, id_task, files)
        self.operations.append(func)
        return func()

    def upload_json_files(self, id_task: int, files: dict):
        func = partial(self.__api.upload_json_files, id_task, files)
        self.operations.append(func)
        return func()

    def delete_file(self, id_task: int, filename: str):
        func = partial(self.__api.delete_file, id_task, filename)
        self.operations.append(func)
        return func()

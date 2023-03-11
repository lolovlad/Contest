from typing import List
from Classes.ProxyController import TaskProxy
from Classes.Models.TypeNotify import TypeNotify
from Classes.Models.Task import TaskPost, TaskSettings
import eel


class TaskPage:
    def __init__(self, id_contest: int):
        self.__proxy_task: TaskProxy = TaskProxy()
        self.__id_contest: int = id_contest
        self.__id_task: int = 0
        self.__mode_update: bool = False
        self.__file_templates: dict = {
            "main": "templates/task.html",
            "form": "templates/task_form.html",
            "form_settings": "templates/task_settings_form.html"
                                       }

    def show_view(self, **kwargs):
        self.__mode_update = False
        eel.locationReplace(self.__file_templates["main"])

    def show_view_form(self):
        self.__mode_update = False
        eel.locationReplace(self.__file_templates["form"])

    def show_view_form_update(self, id_task: int):
        self.__id_task = id_task
        self.__mode_update = True
        eel.locationReplace(self.__file_templates["form"])

    def show_view_form_settings(self, id_task: int):
        self.__id_task = id_task
        self.__mode_update = False
        eel.locationReplace(self.__file_templates["form_settings"])

    def get_mode_update(self):
        return self.__mode_update

    def get_list_task_in_contest(self) -> List[dict]:
        return self.__proxy_task.get_list_task(self.__id_contest)

    def get_task(self):
        return self.__proxy_task.get_task(self.__id_task)

    def get_settings(self) -> dict:
        return self.__proxy_task.get_settings(self.__id_task)

    def add_task(self, task: dict):
        task["id_contest"] = self.__id_contest
        task = TaskPost(**task)
        self.__proxy_task.post_task(task)
        self.show_view()

    def update_setting(self, settings: dict):
        task = TaskSettings(**settings)
        self.__proxy_task.put_settings_task(task)
        self.show_view()

    def add_files(self, list_name_file: List[str]):
        new_name_file_list = []
        for name in list_name_file:
            new_name_file = name.split("/")
            files = {
                "file": open(name, "rb"),
                "filename": new_name_file[-1]
            }
            response = self.__proxy_task.upload_files(self.__id_task, files)
            new_name_file_list.append(new_name_file[-1])
        return new_name_file_list

    def delete_file(self, name_file: str):
        response = self.__proxy_task.delete_file(self.__id_task, name_file)

    def upload_json_file(self, file_name: str):
        new_name_file = file_name.split("/")
        files = {
            "file": open(file_name, "rb"),
            "filename": new_name_file[-1]
        }
        response = self.__proxy_task.upload_json_files(self.__id_task, files)
        return new_name_file[-1]

    def delete_task(self, id_task: int):
        response = self.__proxy_task.delete_task(id_task)
        self.show_view()

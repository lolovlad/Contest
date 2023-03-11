from abc import ABC, abstractmethod


class Task(ABC):
    @abstractmethod
    def post_task(self, *args, **kwargs):
        pass

    @abstractmethod
    def put_task(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_task(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_list_task(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_task(self, *args, **kwargs):
        pass

    @abstractmethod
    def put_settings_task(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_settings(self, *args, **kwargs):
        pass

    @abstractmethod
    def upload_files(self, *args, **kwargs):
        pass

    @abstractmethod
    def upload_json_files(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_file(self, *args, **kwargs):
        pass

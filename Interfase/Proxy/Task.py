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

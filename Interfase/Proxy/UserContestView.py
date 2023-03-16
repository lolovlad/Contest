from abc import ABC, abstractmethod


class UserContestView(ABC):
    @abstractmethod
    def get_contest(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_list_task(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_task(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_list_answers(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_report(self, *args, **kwargs):
        pass

    @abstractmethod
    def close_contest(self, *args, **kwargs):
        pass
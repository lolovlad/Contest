from abc import ABC, abstractmethod


class Answers(ABC):
    @abstractmethod
    def get_package(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_answers(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_report(self, *args, **kwargs):
        pass

    @abstractmethod
    def post_answers(self, *args, **kwargs):
        pass

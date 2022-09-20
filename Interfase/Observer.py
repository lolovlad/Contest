from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, type_notify):
        pass


class Subject(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, type_notify):
        pass

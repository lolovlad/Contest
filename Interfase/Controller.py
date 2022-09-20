from abc import abstractmethod, ABC


class Controller(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def show_view(self, **kwargs):
        pass



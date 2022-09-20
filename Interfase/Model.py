from abc import abstractmethod, ABC


class Model(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass

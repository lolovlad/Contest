from abc import ABC, abstractmethod


class Menu(ABC):

    @abstractmethod
    def load_to_database_contest(self, data):
        pass
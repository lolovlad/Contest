from abc import ABC, abstractmethod


class Main(ABC):

    @abstractmethod
    def load_to_database_json_test_file(self, data):
        pass

    @abstractmethod
    def load_to_database_answers(self, data):
        pass

    @abstractmethod
    def add_answer(self, data):
        pass

    @abstractmethod
    def update_team(self, data):
        pass

    @abstractmethod
    def load_to_database_json_report(self, data):
        pass
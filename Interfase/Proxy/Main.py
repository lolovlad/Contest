from abc import ABC, abstractmethod


class Main(ABC):

    @abstractmethod
    def load_to_database_contest_page(self, data):
        pass

    @abstractmethod
    def load_to_database_answers(self, data):
        pass

    @abstractmethod
    def load_to_database_package(self, data):
        pass

    @abstractmethod
    def add_answer(self, data):
        pass

    @abstractmethod
    def load_to_database_json_report(self, data):
        pass

    @abstractmethod
    def load_to_database_compilation(self, data):
        pass

    @abstractmethod
    def get_status_user(self, data):
        pass

    @abstractmethod
    def close_contest_to_user(self, data):
        pass

from abc import ABC, abstractmethod


class AdminPanel(ABC):

    @abstractmethod
    def add_user(self, data):
        pass

    @abstractmethod
    def delete_user(self, data):
        pass

    @abstractmethod
    def update_user(self, data):
        pass

    @abstractmethod
    def load_to_database_user(self, data):
        pass

    @abstractmethod
    def add_contest(self, data):
        pass

    @abstractmethod
    def delete_contest(self, data):
        pass

    @abstractmethod
    def update_contest(self, data):
        pass

    @abstractmethod
    def load_to_database_contest(self, data):
        pass

    @abstractmethod
    def add_task(self, data):
        pass

    @abstractmethod
    def delete_task(self, data):
        pass

    @abstractmethod
    def update_task(self, data):
        pass

    @abstractmethod
    def load_to_database_team(self, data):
        pass

    @abstractmethod
    def add_team(self, data):
        pass

    @abstractmethod
    def delete_team(self, data):
        pass

    @abstractmethod
    def update_team(self, data):
        pass

    @abstractmethod
    def load_to_database_report_total(self, data):
        pass

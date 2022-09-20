from abc import ABC, abstractmethod


class User(ABC):

    @abstractmethod
    def get_users(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_status_user(self, *args, **kwargs):
        pass

    @abstractmethod
    def post_user(self, *args, **kwargs):
        pass

    @abstractmethod
    def put_user(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_user(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_in_team_users(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_in_contest_users(self, *args, **kwargs):
        pass

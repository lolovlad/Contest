from abc import ABC, abstractmethod


class Team(ABC):
    @abstractmethod
    def get_team(self, *args, **kwargs):
        pass

    @abstractmethod
    def post_team(self, *args, **kwargs):
        pass

    @abstractmethod
    def put_team(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_team(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_list_team_in_contest(self, *args, **kwargs):
        pass
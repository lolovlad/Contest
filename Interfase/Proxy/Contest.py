from abc import ABC, abstractmethod


class Contest(ABC):
    @abstractmethod
    def get_list_contest(self, *args, **kwargs):
        pass

    @abstractmethod
    def post_contest(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_contest(self, *args, **kwargs):
        pass

    @abstractmethod
    def update_contest(self, *args, **kwargs):
        pass

    @abstractmethod
    def registration_users_contest(self, *args, **kwargs):
        pass

    @abstractmethod
    def contests_by_user_id(self, *args, **kwargs):
        pass

    @abstractmethod
    def contest_page(self, *args, **kwargs):
        pass

    @abstractmethod
    def close_to_user_contest(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_report_total(self, *args, **kwargs):
        pass

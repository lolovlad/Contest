from abc import ABC, abstractmethod


class EducationalOrganizations(ABC):
    @abstractmethod
    def get_organizations(self, *args, **kwargs):
        pass

    @abstractmethod
    def post_organizations(self, *args, **kwargs):
        pass

    @abstractmethod
    def put_organizations(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_organizations(self, *args, **kwargs):
        pass

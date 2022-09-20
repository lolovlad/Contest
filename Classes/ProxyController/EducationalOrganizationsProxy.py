from Interfase.Proxy.EducationalOrganizations import EducationalOrganizations
from Classes.ProxyController.EducationalOrganizationsAPI import EducationalOrganizationsAPI
from functools import partial


class EducationalOrganizationsProxy(EducationalOrganizations):
    def __init__(self, api: EducationalOrganizationsAPI = EducationalOrganizationsAPI()):
        self.__api = api
        self.operations = []

    def get_organizations(self):
        func = partial(self.__api.get_organizations)
        self.operations.append(func)
        return func()

    def post_organizations(self, *args, **kwargs):
        pass

    def put_organizations(self, *args, **kwargs):
        pass

    def delete_organizations(self, *args, **kwargs):
        pass


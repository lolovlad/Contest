from typing import List
from Interfase.Proxy.EducationalOrganizations import EducationalOrganizations
from Classes.RequestsAPI import RequestsAPI


class EducationalOrganizationsAPI(EducationalOrganizations):
    def __init__(self, api: RequestsAPI = RequestsAPI()):
        self.__api = api

    def get_organizations(self) -> List[dict]:
        return self.__api.get("educational_organizations", {})

    def post_organizations(self, *args, **kwargs):
        pass

    def put_organizations(self, *args, **kwargs):
        pass

    def delete_organizations(self, *args, **kwargs):
        pass
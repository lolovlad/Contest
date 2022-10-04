import requests
from settings import settings


class RequestsAPI:
    def __init__(self, key=None):
        self.__headers = {"Authorization": f"Bearer {key}"}
        self.__BASEADDRESS = f"http://{settings.host_server}:{settings.port_server}"

    def post(self, request: str, data, *args, **kwargs):
        response = requests.post(f"{self.__BASEADDRESS}/{request}", json=data, *args, **kwargs)
        return response.json()

    def get(self, request: str, data: dict, *args, **kwargs):
        response = self.__response(requests.get, request, data, *args, **kwargs)
        return response

    def delete(self, request: str, data: dict, *args, **kwargs):
        response = requests.delete(f"{self.__BASEADDRESS}/{request}", *args, **kwargs)
        response_json = response.json()
        return response_json

    def put(self, request: str, data: dict, *args, **kwargs):
        response = requests.put(f"{self.__BASEADDRESS}/{request}", json=data, *args, **kwargs)
        return response.json()

    def post_token(self, request: str, data: dict, *args, **kwargs):
        response = requests.post(f"{self.__BASEADDRESS}/{request}", headers=self.__headers, json=data, *args, **kwargs)
        return response.json()

    def get_toke(self, request: str, data: dict, *args, **kwargs):
        response = self.__response(requests.get, request, headers=self.__headers, data=data, *args, **kwargs)
        return response

    def delete_toke(self, request: str, data: dict, *args, **kwargs):
        response = requests.delete(f"{self.__BASEADDRESS}/{request}", headers=self.__headers, *args, **kwargs)
        response_json = response.json()
        return response_json

    def put_token(self, request: str, data: dict, *args, **kwargs):
        response = requests.put(f"{self.__BASEADDRESS}/{request}", headers=self.__headers, json=data, *args, **kwargs)
        return response.json()

    def __response(self, type_response, request: str, data, *args, **kwargs):
        response = type_response(f"{self.__BASEADDRESS}/{request}", data, *args, **kwargs)
        return response.json()

    def post_sign_in(self, request, data):
        payload = f"grant_type=&username={data['login']}&password={data['password']}&client_id=&client_secret="

        response = requests.post(
            f"{self.__BASEADDRESS}/{request}",
            headers={'Content-Type': 'application/x-www-form-urlencoded', 'accept': 'application/json'},
            data=payload,
        )
        return response.json()


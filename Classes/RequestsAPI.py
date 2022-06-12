import requests


class RequestsAPI:
    def __init__(self, key):
        self.__BASEADDRESS = "http://192.168.31.231:2000"
        self.__key = key

    def post(self, request: str, data: dict, *args, **kwargs):
        response = self.__response(requests.post, request, data, *args, **kwargs)
        return response

    def get(self, request: str, data: dict, *args, **kwargs):
        response = self.__response(requests.get, request, data, *args, **kwargs)
        return response

    def delete(self, request: str, data: dict, *args, **kwargs):
        response = requests.delete(f"{self.__BASEADDRESS}/{request}", *args, **kwargs)
        response_json = response.json()
        return response_json

    def put(self, request: str, data: dict, *args, **kwargs):
        response = self.__response(requests.put, request, data, *args, **kwargs)
        return response

    def __response(self, type_response, request: str, data, *args, **kwargs):
        data["key"] = self.__key
        response = type_response(f"{self.__BASEADDRESS}/{request}", data, *args, **kwargs)
        response_json = response.json()
        return response_json

import requests
from config.settings import BASE_URL

class ApiClient:
    @staticmethod
    def get(endpoint, **kwargs):
        url = f"{BASE_URL}/{endpoint}"
        return requests.get(url, **kwargs)

    @staticmethod
    def post(endpoint, json=None, **kwargs):
        url = f"{BASE_URL}/{endpoint}"
        return requests.post(url, json=json, **kwargs)

    @staticmethod
    def put(endpoint, json=None, **kwargs):
        url = f"{BASE_URL}/{endpoint}"
        return requests.put(url, json=json, **kwargs)

    @staticmethod
    def delete(endpoint, **kwargs):
        url = f"{BASE_URL}/{endpoint}"
        return requests.delete(url, **kwargs)
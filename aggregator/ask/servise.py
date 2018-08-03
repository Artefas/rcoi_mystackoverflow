import requests
from requests import ConnectionError, ConnectTimeout

class Service:
    _host = ""
    _port = ""

    def __init__(self, host, port):
        _host = host
        _port = port

    def get(self, url, params=None):
        url = self._host + ":" + self._port + url
        return requests.get(url=url,params=params)

    def post(self, url, data=None, json=None):
        return requests.post(url=url,data=data, json=json)

    def put(self, url, data, json):
        return requests.put(url=url,data=data,json=json)

    def patch(self):
        pass
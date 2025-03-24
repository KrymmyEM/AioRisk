import urllib
from aiohttp import BasicAuth

class App:
    def __init__(self, uri: str, login: str, password: str, name: str):
        self._uri = uri
        self._login = login
        self._password = password
        self.name = name

    @property
    def events_uri(self):
        uri = urllib.parse.urlparse(self.url)
        to_scheme = {
            "http": "ws",
            "https": "wss",
            "ws": "ws",
            "wss": "wss",
        }
        return f"{to_scheme[uri.scheme]}://{uri.netloc}{uri.path}/events?api_key={self._login}:{self._password}&app={self.name}"
    
    @property
    def url(self):
        return self._uri.strip("/")

    @property
    def auth(self):
        return BasicAuth(login=self._login, password=self._password)

import asyncio
import aiohttp
from aiohttp import BasicAuth
import json
from urllib.parse import urlparse, urljoin
from typing import Union, Optional

from ..base.api_client import ApiClient
from ..base.app import App
from ..models_api import *
from ..models_api.Response import Response as AsteriskResponse
from ..models.base_models import Channel

class ARIClient(ApiClient):
    def __init__(self, url: str, login: str, password: str, app: Optional[App] = None):
        self.url = url
        self.auth = BasicAuth(login=login, password=password)
        self.app = app
        self.asterisk = AsteriskAPI(self)
        self.endpoints = EndpointAPI(self)
        self.channels = ChannelAPI(self)
        self.bridges = BridgeAPI(self)
        self.recordings = RecordingAPI(self)
        self.sounds = SoundAPI(self)
        self.playback = PlaybackControlAPI(self)
        self.devices = DeviceStateAPI(self)
        self.mailboxes = MailboxesAPI(self)
        self.events = WebsocketResource(self)
        self.stasis = StasisApplicationAPI(self)


    async def _request(self, method, url, params: dict = {}, json_data: dict = {},):
        url = url.strip("/")
        async with aiohttp.ClientSession(auth=self.auth) as session:
            async with session.request(method, url, params=params, json=json_data) as response:
                if response.status == 401:
                    raise AsteriskError(401, "Unauthorized")
                
                if response.content_length == 0:
                    return AsteriskResponse(response.status, {})
                content_type_funcs = {
                    "application/json": response.json,
                    "text/plain": response.text,
                    "application/xml": response.text,
                    "audio/wav": response.read
                }
                if response.content_type == "application/json":
                    return AsteriskResponse(response.status, await response.json())
                
                return AsteriskResponse(response.status, await content_type_funcs[response.content_type]())


    async def post(self, url, params: dict = {}, json_data: dict = {}):
        return await self._request("POST", url, params, json_data)

    async def get(self, url, params: dict = {}, json_data: dict = {}):
        return await self._request("GET", url, params, json_data)

    async def delete(self, url, params: dict = {}, json_data: dict = {}):
        return await self._request("DELETE", url, params, json_data)

    async def put(self, url, params: dict = {}, json_data: dict = {}):
        return await self._request("PUT", url, params, json_data)
        

    @property
    def base_url(self):
        return self.url
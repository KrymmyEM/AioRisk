from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class BridgeAPI(ResourceAPI):

    async def list(self, ):
        request_to="/bridges"
        data = {}

        # TODO: implement list logic
        json_params = {}
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return [Bridge(**item) for item in response_data]

    async def create(self, **kwargs):
        request_to="/bridges"
        data = {}

        optionals = {
             "type": {"data_type": str, "default": "None"},
             "bridgeId": {"data_type": str, "default": "None"},
             "name": {"data_type": str, "default": "None"},
        }

        for key, value in kwargs.items():
            if key in optionals:
                if value is None:
                    if optionals[key]['defaulf']:
                        data[key] = optionals[key]['default']
                    continue
                if not isinstance(value, optionals[key]['data_type']):
                    raise TypeError(f'{key} must be {optionals[key]['data_type']}')
                if optionals[key]['data_type'] is bool:
                    value = str(value).lower()
                data[key] = value
            else:
                continue
        # TODO: implement create logic
        json_params = {}
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Bridge(**response_data)

    async def createWithId(self, bridgeId: str, **kwargs):
        request_to="/bridges/{bridgeId}"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        data = {}

        optionals = {
             "type": {"data_type": str, "default": "None"},
             "name": {"data_type": str, "default": "None"},
        }

        for key, value in kwargs.items():
            if key in optionals:
                if value is None:
                    if optionals[key]['defaulf']:
                        data[key] = optionals[key]['default']
                    continue
                if not isinstance(value, optionals[key]['data_type']):
                    raise TypeError(f'{key} must be {optionals[key]['data_type']}')
                if optionals[key]['data_type'] is bool:
                    value = str(value).lower()
                data[key] = value
            else:
                continue
        # TODO: implement createWithId logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Bridge(**response_data)

    async def get(self, bridgeId: str, ):
        request_to="/bridges/{bridgeId}"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        data = {}

        # TODO: implement get logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Bridge not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Bridge(**response_data)

    async def destroy(self, bridgeId: str, ):
        request_to="/bridges/{bridgeId}"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        data = {}

        # TODO: implement destroy logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Bridge not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def addChannel(self, bridgeId: str, channel: str, **kwargs):
        request_to="/bridges/{bridgeId}/addChannel"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        if not isinstance(channel, str):
            raise TypeError(f'channel must be str')

        data = {}

        optionals = {
             "role": {"data_type": str, "default": "None"},
             "absorbDTMF": {"data_type": bool, "default": "false"},
             "mute": {"data_type": bool, "default": "false"},
             "inhibitConnectedLineUpdates": {"data_type": bool, "default": "false"},
        }

        for key, value in kwargs.items():
            if key in optionals:
                if value is None:
                    if optionals[key]['defaulf']:
                        data[key] = optionals[key]['default']
                    continue
                if not isinstance(value, optionals[key]['data_type']):
                    raise TypeError(f'{key} must be {optionals[key]['data_type']}')
                if optionals[key]['data_type'] is bool:
                    value = str(value).lower()
                data[key] = value
            else:
                continue
        # TODO: implement addChannel logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        data['channel']=channel
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Channel not found",
            404: "Bridge not found",
            409: "Bridge not in Stasis application; Channel currently recording",
            422: "Channel not in Stasis application",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def removeChannel(self, bridgeId: str, channel: str, ):
        request_to="/bridges/{bridgeId}/removeChannel"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        if not isinstance(channel, str):
            raise TypeError(f'channel must be str')

        data = {}

        # TODO: implement removeChannel logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        data['channel']=channel
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Channel not found",
            404: "Bridge not found",
            409: "Bridge not in Stasis application",
            422: "Channel not in this bridge",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def setVideoSource(self, bridgeId: str, channelId: str, ):
        request_to="/bridges/{bridgeId}/videoSource/{channelId}"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement setVideoSource logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Bridge or Channel not found",
            409: "Channel not in Stasis application",
            422: "Channel not in this Bridge",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def clearVideoSource(self, bridgeId: str, ):
        request_to="/bridges/{bridgeId}/videoSource"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        data = {}

        # TODO: implement clearVideoSource logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Bridge not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def startMoh(self, bridgeId: str, **kwargs):
        request_to="/bridges/{bridgeId}/moh"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        data = {}

        optionals = {
             "mohClass": {"data_type": str, "default": "None"},
        }

        for key, value in kwargs.items():
            if key in optionals:
                if value is None:
                    if optionals[key]['defaulf']:
                        data[key] = optionals[key]['default']
                    continue
                if not isinstance(value, optionals[key]['data_type']):
                    raise TypeError(f'{key} must be {optionals[key]['data_type']}')
                if optionals[key]['data_type'] is bool:
                    value = str(value).lower()
                data[key] = value
            else:
                continue
        # TODO: implement startMoh logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Bridge not found",
            409: "Bridge not in Stasis application",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def stopMoh(self, bridgeId: str, ):
        request_to="/bridges/{bridgeId}/moh"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        data = {}

        # TODO: implement stopMoh logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Bridge not found",
            409: "Bridge not in Stasis application",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def play(self, bridgeId: str, media: str, **kwargs):
        request_to="/bridges/{bridgeId}/play"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        if not isinstance(media, str):
            raise TypeError(f'media must be str')

        data = {}

        optionals = {
             "lang": {"data_type": str, "default": "None"},
             "offsetms": {"data_type": int, "default": 0},
             "skipms": {"data_type": int, "default": 3000},
             "playbackId": {"data_type": str, "default": "None"},
        }

        for key, value in kwargs.items():
            if key in optionals:
                if value is None:
                    if optionals[key]['defaulf']:
                        data[key] = optionals[key]['default']
                    continue
                if not isinstance(value, optionals[key]['data_type']):
                    raise TypeError(f'{key} must be {optionals[key]['data_type']}')
                if optionals[key]['data_type'] is bool:
                    value = str(value).lower()
                data[key] = value
            else:
                continue
        # TODO: implement play logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        data['media']=media
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Bridge not found",
            409: "Bridge not in a Stasis application",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Playback(**response_data)

    async def playWithId(self, bridgeId: str, playbackId: str, media: str, **kwargs):
        request_to="/bridges/{bridgeId}/play/{playbackId}"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        if not isinstance(playbackId, str):
            raise TypeError(f'playbackId must be str')

        if not isinstance(media, str):
            raise TypeError(f'media must be str')

        data = {}

        optionals = {
             "lang": {"data_type": str, "default": "None"},
             "offsetms": {"data_type": int, "default": 0},
             "skipms": {"data_type": int, "default": 3000},
        }

        for key, value in kwargs.items():
            if key in optionals:
                if value is None:
                    if optionals[key]['defaulf']:
                        data[key] = optionals[key]['default']
                    continue
                if not isinstance(value, optionals[key]['data_type']):
                    raise TypeError(f'{key} must be {optionals[key]['data_type']}')
                if optionals[key]['data_type'] is bool:
                    value = str(value).lower()
                data[key] = value
            else:
                continue
        # TODO: implement playWithId logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        request_to = request_to.replace('{playbackId}', str(playbackId))
        data['media']=media
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Bridge not found",
            409: "Bridge not in a Stasis application",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Playback(**response_data)

    async def record(self, bridgeId: str, name: str, format: str, **kwargs):
        request_to="/bridges/{bridgeId}/record"
        if not isinstance(bridgeId, str):
            raise TypeError(f'bridgeId must be str')

        if not isinstance(name, str):
            raise TypeError(f'name must be str')

        if not isinstance(format, str):
            raise TypeError(f'format must be str')

        data = {}

        optionals = {
             "maxDurationSeconds": {"data_type": int, "default": 0},
             "maxSilenceSeconds": {"data_type": int, "default": 0},
             "ifExists": {"data_type": str, "default": "fail"},
             "beep": {"data_type": bool, "default": "false"},
             "terminateOn": {"data_type": str, "default": "none"},
        }

        for key, value in kwargs.items():
            if key in optionals:
                if value is None:
                    if optionals[key]['defaulf']:
                        data[key] = optionals[key]['default']
                    continue
                if not isinstance(value, optionals[key]['data_type']):
                    raise TypeError(f'{key} must be {optionals[key]['data_type']}')
                if optionals[key]['data_type'] is bool:
                    value = str(value).lower()
                data[key] = value
            else:
                continue
        # TODO: implement record logic
        json_params = {}
        request_to = request_to.replace('{bridgeId}', str(bridgeId))
        data['name']=name
        data['format']=format
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters",
            404: "Bridge not found",
            409: "Bridge is not in a Stasis application; A recording with the same name already exists on the system and can not be overwritten because it is in progress or ifExists=fail",
            422: "The format specified is unknown on this system",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return LiveRecording(**response_data)
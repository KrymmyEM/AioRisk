from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class ChannelAPI(ResourceAPI):

    async def list(self, ):
        request_to="/channels"
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
        return [Channel(**item) for item in response_data]

    async def originate(self, endpoint: str, **kwargs):
        request_to="/channels"
        if not isinstance(endpoint, str):
            raise TypeError(f'endpoint must be str')

        data = {}

        optionals = {
             "extension": {"data_type": str, "default": "None"},
             "context": {"data_type": str, "default": "None"},
             "priority": {"data_type": int, "default": None},
             "label": {"data_type": str, "default": "None"},
             "app": {"data_type": str, "default": "None"},
             "appArgs": {"data_type": str, "default": "None"},
             "callerId": {"data_type": str, "default": "None"},
             "timeout": {"data_type": int, "default": 30},
             "variables": {"data_type": dict, "default": None},
             "channelId": {"data_type": str, "default": "None"},
             "otherChannelId": {"data_type": str, "default": "None"},
             "originator": {"data_type": str, "default": "None"},
             "formats": {"data_type": str, "default": "None"},
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
        # TODO: implement originate logic
        json_params = {}
        data['endpoint']=endpoint
        variables = data.pop('variables', None)
        if variables:
            json_params.update(variables)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters for originating a channel.",
            409: "Channel with given unique ID already exists.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Channel(**response_data)

    async def create(self, endpoint: str, app: str, **kwargs):
        request_to="/channels/create"
        if not isinstance(endpoint, str):
            raise TypeError(f'endpoint must be str')

        if not isinstance(app, str):
            raise TypeError(f'app must be str')

        data = {}

        optionals = {
             "appArgs": {"data_type": str, "default": "None"},
             "channelId": {"data_type": str, "default": "None"},
             "otherChannelId": {"data_type": str, "default": "None"},
             "originator": {"data_type": str, "default": "None"},
             "formats": {"data_type": str, "default": "None"},
             "variables": {"data_type": dict, "default": None},
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
        data['endpoint']=endpoint
        data['app']=app
        variables = data.pop('variables', None)
        if variables:
            json_params.update(variables)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            409: "Channel with given unique ID already exists.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Channel(**response_data)

    async def get(self, channelId: str, ):
        request_to="/channels/{channelId}"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement get logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Channel(**response_data)

    async def originateWithId(self, channelId: str, endpoint: str, **kwargs):
        request_to="/channels/{channelId}"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        if not isinstance(endpoint, str):
            raise TypeError(f'endpoint must be str')

        data = {}

        optionals = {
             "extension": {"data_type": str, "default": "None"},
             "context": {"data_type": str, "default": "None"},
             "priority": {"data_type": int, "default": None},
             "label": {"data_type": str, "default": "None"},
             "app": {"data_type": str, "default": "None"},
             "appArgs": {"data_type": str, "default": "None"},
             "callerId": {"data_type": str, "default": "None"},
             "timeout": {"data_type": int, "default": 30},
             "variables": {"data_type": dict, "default": None},
             "otherChannelId": {"data_type": str, "default": "None"},
             "originator": {"data_type": str, "default": "None"},
             "formats": {"data_type": str, "default": "None"},
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
        # TODO: implement originateWithId logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        data['endpoint']=endpoint
        variables = data.pop('variables', None)
        if variables:
            json_params.update(variables)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters for originating a channel.",
            409: "Channel with given unique ID already exists.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Channel(**response_data)

    async def hangup(self, channelId: str, **kwargs):
        request_to="/channels/{channelId}"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        optionals = {
             "reason_code": {"data_type": str, "default": "None"},
             "reason": {"data_type": str, "default": "None"},
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
        # TODO: implement hangup logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid reason for hangup provided",
            404: "Channel not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def continueInDialplan(self, channelId: str, **kwargs):
        request_to="/channels/{channelId}/continue"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        optionals = {
             "context": {"data_type": str, "default": "None"},
             "extension": {"data_type": str, "default": "None"},
             "priority": {"data_type": int, "default": None},
             "label": {"data_type": str, "default": "None"},
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
        # TODO: implement continueInDialplan logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def move(self, channelId: str, app: str, **kwargs):
        request_to="/channels/{channelId}/move"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        if not isinstance(app, str):
            raise TypeError(f'app must be str')

        data = {}

        optionals = {
             "appArgs": {"data_type": str, "default": "None"},
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
        # TODO: implement move logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        data['app']=app
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def redirect(self, channelId: str, endpoint: str, ):
        request_to="/channels/{channelId}/redirect"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        if not isinstance(endpoint, str):
            raise TypeError(f'endpoint must be str')

        data = {}

        # TODO: implement redirect logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        data['endpoint']=endpoint
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Endpoint parameter not provided",
            404: "Channel or endpoint not found",
            409: "Channel not in a Stasis application",
            422: "Endpoint is not the same type as the channel",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def answer(self, channelId: str, ):
        request_to="/channels/{channelId}/answer"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement answer logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def ring(self, channelId: str, ):
        request_to="/channels/{channelId}/ring"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement ring logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def ringStop(self, channelId: str, ):
        request_to="/channels/{channelId}/ring"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement ringStop logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def sendDTMF(self, channelId: str, **kwargs):
        request_to="/channels/{channelId}/dtmf"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        optionals = {
             "dtmf": {"data_type": str, "default": "None"},
             "before": {"data_type": int, "default": 0},
             "between": {"data_type": int, "default": 100},
             "duration": {"data_type": int, "default": 100},
             "after": {"data_type": int, "default": 0},
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
        # TODO: implement sendDTMF logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "DTMF is required",
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def mute(self, channelId: str, **kwargs):
        request_to="/channels/{channelId}/mute"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        optionals = {
             "direction": {"data_type": str, "default": "both"},
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
        # TODO: implement mute logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def unmute(self, channelId: str, **kwargs):
        request_to="/channels/{channelId}/mute"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        optionals = {
             "direction": {"data_type": str, "default": "both"},
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
        # TODO: implement unmute logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def hold(self, channelId: str, ):
        request_to="/channels/{channelId}/hold"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement hold logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def unhold(self, channelId: str, ):
        request_to="/channels/{channelId}/hold"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement unhold logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def startMoh(self, channelId: str, **kwargs):
        request_to="/channels/{channelId}/moh"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

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
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def stopMoh(self, channelId: str, ):
        request_to="/channels/{channelId}/moh"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement stopMoh logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def startSilence(self, channelId: str, ):
        request_to="/channels/{channelId}/silence"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement startSilence logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def stopSilence(self, channelId: str, ):
        request_to="/channels/{channelId}/silence"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement stopSilence logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def play(self, channelId: str, media: str, **kwargs):
        request_to="/channels/{channelId}/play"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        if not isinstance(media, str):
            raise TypeError(f'media must be str')

        data = {}

        optionals = {
             "lang": {"data_type": str, "default": "None"},
             "offsetms": {"data_type": int, "default": None},
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
        request_to = request_to.replace('{channelId}', str(channelId))
        data['media']=media
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Playback(**response_data)

    async def playWithId(self, channelId: str, playbackId: str, media: str, **kwargs):
        request_to="/channels/{channelId}/play/{playbackId}"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        if not isinstance(playbackId, str):
            raise TypeError(f'playbackId must be str')

        if not isinstance(media, str):
            raise TypeError(f'media must be str')

        data = {}

        optionals = {
             "lang": {"data_type": str, "default": "None"},
             "offsetms": {"data_type": int, "default": None},
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
        request_to = request_to.replace('{channelId}', str(channelId))
        request_to = request_to.replace('{playbackId}', str(playbackId))
        data['media']=media
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel not found",
            409: "Channel not in a Stasis application",
            412: "Channel in invalid state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Playback(**response_data)

    async def record(self, channelId: str, name: str, format: str, **kwargs):
        """
        Record the audio from a channel.

        Args:
            channelId (str): The id of the channel to record.
            name (str): The name of the file to record to.
            format (str): The format of the file to record to.
            maxDurationSeconds (int): The maximum duration of the recording in
                seconds. 0 means no limit. Defaults to 0.
            maxSilenceSeconds (int): The maximum duration of silence in seconds.
                0 means no limit. Defaults to 0.
            ifExists (str): The action to take if a file with the same name
                already exists. One of "fail", "overwrite", or "append".
                Defaults to "fail".
            beep (bool): Whether to play a beep at the start of the recording.
                Defaults to False.
            terminateOn (str): DTMF input to terminate the recording. One of
                "none", "any", or a specific DTMF digit. Defaults to "none".

        Returns:
            LiveRecording: The recording object.

        Raises:
            AsteriskError: If there is an error communicating with the Asterisk
                server.
        """
        request_to="/channels/{channelId}/record"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

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
        request_to = request_to.replace('{channelId}', str(channelId))
        data['name']=name
        data['format']=format
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters",
            404: "Channel not found",
            409: "Channel is not in a Stasis application; the channel is currently bridged with other hcannels; A recording with the same name already exists on the system and can not be overwritten because it is in progress or ifExists=fail",
            422: "The format specified is unknown on this system",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return LiveRecording(**response_data)

    async def getChannelVar(self, channelId: str, variable: str, ):
        request_to="/channels/{channelId}/variable"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        if not isinstance(variable, str):
            raise TypeError(f'variable must be str')

        data = {}

        # TODO: implement getChannelVar logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        data['variable']=variable
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Missing variable parameter.",
            404: "Channel or variable not found",
            409: "Channel not in a Stasis application",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Variable(**response_data)

    async def setChannelVar(self, channelId: str, variable: str, **kwargs):
        request_to="/channels/{channelId}/variable"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        if not isinstance(variable, str):
            raise TypeError(f'variable must be str')

        data = {}

        optionals = {
             "value": {"data_type": str, "default": "None"},
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
        # TODO: implement setChannelVar logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        data['variable']=variable
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Missing variable parameter.",
            404: "Channel not found",
            409: "Channel not in a Stasis application",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def snoopChannel(self, channelId: str, app: str, **kwargs):
        request_to="/channels/{channelId}/snoop"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        if not isinstance(app, str):
            raise TypeError(f'app must be str')

        data = {}

        optionals = {
             "spy": {"data_type": str, "default": "none"},
             "whisper": {"data_type": str, "default": "none"},
             "appArgs": {"data_type": str, "default": "None"},
             "snoopId": {"data_type": str, "default": "None"},
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
        # TODO: implement snoopChannel logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        data['app']=app
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters",
            404: "Channel not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Channel(**response_data)

    async def snoopChannelWithId(self, channelId: str, snoopId: str, app: str, **kwargs):
        request_to="/channels/{channelId}/snoop/{snoopId}"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        if not isinstance(snoopId, str):
            raise TypeError(f'snoopId must be str')

        if not isinstance(app, str):
            raise TypeError(f'app must be str')

        data = {}

        optionals = {
             "spy": {"data_type": str, "default": "none"},
             "whisper": {"data_type": str, "default": "none"},
             "appArgs": {"data_type": str, "default": "None"},
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
        # TODO: implement snoopChannelWithId logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        request_to = request_to.replace('{snoopId}', str(snoopId))
        data['app']=app
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters",
            404: "Channel not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Channel(**response_data)

    async def dial(self, channelId: str, **kwargs):
        request_to="/channels/{channelId}/dial"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        optionals = {
             "caller": {"data_type": str, "default": "None"},
             "timeout": {"data_type": int, "default": 0},
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
        # TODO: implement dial logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel cannot be found.",
            409: "Channel cannot be dialed.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def rtpstatistics(self, channelId: str, ):
        request_to="/channels/{channelId}/rtp_statistics"
        if not isinstance(channelId, str):
            raise TypeError(f'channelId must be str')

        data = {}

        # TODO: implement rtpstatistics logic
        json_params = {}
        request_to = request_to.replace('{channelId}', str(channelId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Channel cannot be found.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return RTPstat(**response_data)

    async def externalMedia(self, app: str, external_host: str, format: str, **kwargs):
        request_to="/channels/externalMedia"
        if not isinstance(app, str):
            raise TypeError(f'app must be str')

        if not isinstance(external_host, str):
            raise TypeError(f'external_host must be str')

        if not isinstance(format, str):
            raise TypeError(f'format must be str')

        data = {}

        optionals = {
             "channelId": {"data_type": str, "default": "None"},
             "variables": {"data_type": dict, "default": None},
             "encapsulation": {"data_type": str, "default": "rtp"},
             "transport": {"data_type": str, "default": "udp"},
             "connection_type": {"data_type": str, "default": "client"},
             "direction": {"data_type": str, "default": "both"},
             "data": {"data_type": str, "default": "None"},
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
        # TODO: implement externalMedia logic
        json_params = {}
        data['app']=app
        data['external_host']=external_host
        data['format']=format
        variables = data.pop('variables', None)
        if variables:
            json_params.update(variables)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters",
            409: "Channel is not in a Stasis application; Channel is already bridged",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Channel(**response_data)
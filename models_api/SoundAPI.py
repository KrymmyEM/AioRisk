from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class SoundAPI(ResourceAPI):

    async def list(self, **kwargs):
        request_to="/sounds"
        data = {}

        optionals = {
             "lang": {"data_type": str, "default": "None"},
             "format": {"data_type": str, "default": "None"},
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
        # TODO: implement list logic
        json_params = {}
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return [Sound(**item) for item in response_data]

    async def get(self, soundId: str, ):
        request_to="/sounds/{soundId}"
        if not isinstance(soundId, str):
            raise TypeError(f'soundId must be str')

        data = {}

        # TODO: implement get logic
        json_params = {}
        request_to = request_to.replace('{soundId}', str(soundId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Sound(**response_data)
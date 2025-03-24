from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class WebsocketResource(ResourceAPI):

    async def eventWebsocket(self, app: str, **kwargs):
        request_to="/events"
        if not isinstance(app, str):
            raise TypeError(f'app must be str')

        data = {}

        optionals = {
             "subscribeAll": {"data_type": bool, "default": "none"},
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
        # TODO: implement eventWebsocket logic
        json_params = {}
        data['app']=app
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Message(**response_data)

    async def userEvent(self, eventName: str, application: str, **kwargs):
        request_to="/events/user/{eventName}"
        if not isinstance(eventName, str):
            raise TypeError(f'eventName must be str')

        if not isinstance(application, str):
            raise TypeError(f'application must be str')

        data = {}

        optionals = {
             "source": {"data_type": str, "default": "None"},
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
        # TODO: implement userEvent logic
        json_params = {}
        request_to = request_to.replace('{eventName}', str(eventName))
        data['application']=application
        variables = data.pop('variables', None)
        if variables:
            json_params.update(variables)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Application does not exist.",
            422: "Event source not found.",
            400: "Invalid even tsource URI or userevent data.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None
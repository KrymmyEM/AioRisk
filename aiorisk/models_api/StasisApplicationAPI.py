from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class StasisApplicationAPI(ResourceAPI):

    async def list(self, ):
        request_to="/applications"
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
        return [Application(**item) for item in response_data]

    async def get(self, applicationName: str, ):
        request_to="/applications/{applicationName}"
        if not isinstance(applicationName, str):
            raise TypeError(f'applicationName must be str')

        data = {}

        # TODO: implement get logic
        json_params = {}
        request_to = request_to.replace('{applicationName}', str(applicationName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Application does not exist.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Application(**response_data)

    async def subscribe(self, applicationName: str, eventSource: str, ):
        request_to="/applications/{applicationName}/subscription"
        if not isinstance(applicationName, str):
            raise TypeError(f'applicationName must be str')

        if not isinstance(eventSource, str):
            raise TypeError(f'eventSource must be str')

        data = {}

        # TODO: implement subscribe logic
        json_params = {}
        request_to = request_to.replace('{applicationName}', str(applicationName))
        data['eventSource']=eventSource
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Missing parameter.",
            404: "Application does not exist.",
            422: "Event source does not exist.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Application(**response_data)

    async def unsubscribe(self, applicationName: str, eventSource: str, ):
        request_to="/applications/{applicationName}/subscription"
        if not isinstance(applicationName, str):
            raise TypeError(f'applicationName must be str')

        if not isinstance(eventSource, str):
            raise TypeError(f'eventSource must be str')

        data = {}

        # TODO: implement unsubscribe logic
        json_params = {}
        request_to = request_to.replace('{applicationName}', str(applicationName))
        data['eventSource']=eventSource
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Missing parameter; event source scheme not recognized.",
            404: "Application does not exist.",
            409: "Application not subscribed to event source.",
            422: "Event source does not exist.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Application(**response_data)

    async def filter(self, applicationName: str, **kwargs):
        request_to="/applications/{applicationName}/eventFilter"
        if not isinstance(applicationName, str):
            raise TypeError(f'applicationName must be str')

        data = {}

        optionals = {
             "filter": {"data_type": dict, "default": None},
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
        # TODO: implement filter logic
        json_params = {}
        request_to = request_to.replace('{applicationName}', str(applicationName))
        filter = data.pop('filter', None)
        if filter:
            json_params.update(filter)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.put(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Bad request.",
            404: "Application does not exist.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Application(**response_data)
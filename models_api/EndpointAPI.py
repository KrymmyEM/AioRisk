from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class EndpointAPI(ResourceAPI):

    async def list(self, ):
        request_to="/endpoints"
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
        return [Endpoint(**item) for item in response_data]

    async def sendMessage(self, to_: str, from_: str, **kwargs):
        request_to="/endpoints/sendMessage"
        if not isinstance(to_, str):
            raise TypeError(f'to_ must be str')

        if not isinstance(from_, str):
            raise TypeError(f'from_ must be str')

        data = {}

        optionals = {
             "body": {"data_type": str, "default": "None"},
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
        # TODO: implement sendMessage logic
        json_params = {}
        data['to']=to_
        data['from']=from_
        variables = data.pop('variables', None)
        if variables:
            json_params.update(variables)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.put(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters for sending a message.",
            404: "Endpoint not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def refer(self, to_: str, from_: str, refer_to: str, **kwargs):
        request_to="/endpoints/refer"
        if not isinstance(to_, str):
            raise TypeError(f'to_ must be str')

        if not isinstance(from_, str):
            raise TypeError(f'from_ must be str')

        if not isinstance(refer_to, str):
            raise TypeError(f'refer_to must be str')

        data = {}

        optionals = {
             "to_self": {"data_type": bool, "default": "false"},
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
        # TODO: implement refer logic
        json_params = {}
        data['to']=to_
        data['from']=from_
        data['refer_to']=refer_to
        variables = data.pop('variables', None)
        if variables:
            json_params.update(variables)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters for referring.",
            404: "Endpoint not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def listByTech(self, tech: str, ):
        request_to="/endpoints/{tech}"
        if not isinstance(tech, str):
            raise TypeError(f'tech must be str')

        data = {}

        # TODO: implement listByTech logic
        json_params = {}
        request_to = request_to.replace('{tech}', str(tech))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Endpoints not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return [Endpoint(**item) for item in response_data]

    async def get(self, tech: str, resource: str, ):
        request_to="/endpoints/{tech}/{resource}"
        if not isinstance(tech, str):
            raise TypeError(f'tech must be str')

        if not isinstance(resource, str):
            raise TypeError(f'resource must be str')

        data = {}

        # TODO: implement get logic
        json_params = {}
        request_to = request_to.replace('{tech}', str(tech))
        request_to = request_to.replace('{resource}', str(resource))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters for sending a message.",
            404: "Endpoints not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Endpoint(**response_data)

    async def sendMessageToEndpoint(self, tech: str, resource: str, from_: str, **kwargs):
        request_to="/endpoints/{tech}/{resource}/sendMessage"
        if not isinstance(tech, str):
            raise TypeError(f'tech must be str')

        if not isinstance(resource, str):
            raise TypeError(f'resource must be str')

        if not isinstance(from_, str):
            raise TypeError(f'from_ must be str')

        data = {}

        optionals = {
             "body": {"data_type": str, "default": "None"},
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
        # TODO: implement sendMessageToEndpoint logic
        json_params = {}
        request_to = request_to.replace('{tech}', str(tech))
        request_to = request_to.replace('{resource}', str(resource))
        data['from']=from_
        variables = data.pop('variables', None)
        if variables:
            json_params.update(variables)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.put(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters for sending a message.",
            404: "Endpoint not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def referToEndpoint(self, tech: str, resource: str, from_: str, refer_to: str, **kwargs):
        request_to="/endpoints/{tech}/{resource}/refer"
        if not isinstance(tech, str):
            raise TypeError(f'tech must be str')

        if not isinstance(resource, str):
            raise TypeError(f'resource must be str')

        if not isinstance(from_, str):
            raise TypeError(f'from_ must be str')

        if not isinstance(refer_to, str):
            raise TypeError(f'refer_to must be str')

        data = {}

        optionals = {
             "to_self": {"data_type": bool, "default": "false"},
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
        # TODO: implement referToEndpoint logic
        json_params = {}
        request_to = request_to.replace('{tech}', str(tech))
        request_to = request_to.replace('{resource}', str(resource))
        data['from']=from_
        data['refer_to']=refer_to
        variables = data.pop('variables', None)
        if variables:
            json_params.update(variables)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Invalid parameters for referring.",
            404: "Endpoint not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None
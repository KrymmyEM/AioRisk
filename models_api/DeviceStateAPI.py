from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class DeviceStateAPI(ResourceAPI):

    async def list(self, ):
        request_to="/deviceStates"
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
        return [DeviceState(**item) for item in response_data]

    async def get(self, deviceName: str, ):
        request_to="/deviceStates/{deviceName}"
        if not isinstance(deviceName, str):
            raise TypeError(f'deviceName must be str')

        data = {}

        # TODO: implement get logic
        json_params = {}
        request_to = request_to.replace('{deviceName}', str(deviceName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return DeviceState(**response_data)

    async def update(self, deviceName: str, deviceState: str, ):
        request_to="/deviceStates/{deviceName}"
        if not isinstance(deviceName, str):
            raise TypeError(f'deviceName must be str')

        if not isinstance(deviceState, str):
            raise TypeError(f'deviceState must be str')

        data = {}

        # TODO: implement update logic
        json_params = {}
        request_to = request_to.replace('{deviceName}', str(deviceName))
        data['deviceState']=deviceState
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.put(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Device name is missing",
            409: "Uncontrolled device specified",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def delete(self, deviceName: str, ):
        request_to="/deviceStates/{deviceName}"
        if not isinstance(deviceName, str):
            raise TypeError(f'deviceName must be str')

        data = {}

        # TODO: implement delete logic
        json_params = {}
        request_to = request_to.replace('{deviceName}', str(deviceName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Device name is missing",
            409: "Uncontrolled device specified",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None
from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class PlaybackControlAPI(ResourceAPI):

    async def get(self, playbackId: str, ):
        request_to="/playbacks/{playbackId}"
        if not isinstance(playbackId, str):
            raise TypeError(f'playbackId must be str')

        data = {}

        # TODO: implement get logic
        json_params = {}
        request_to = request_to.replace('{playbackId}', str(playbackId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "The playback cannot be found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Playback(**response_data)

    async def stop(self, playbackId: str, ):
        request_to="/playbacks/{playbackId}"
        if not isinstance(playbackId, str):
            raise TypeError(f'playbackId must be str')

        data = {}

        # TODO: implement stop logic
        json_params = {}
        request_to = request_to.replace('{playbackId}', str(playbackId))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "The playback cannot be found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def control(self, playbackId: str, operation: str, ):
        request_to="/playbacks/{playbackId}/control"
        if not isinstance(playbackId, str):
            raise TypeError(f'playbackId must be str')

        if not isinstance(operation, str):
            raise TypeError(f'operation must be str')

        data = {}

        # TODO: implement control logic
        json_params = {}
        request_to = request_to.replace('{playbackId}', str(playbackId))
        data['operation']=operation
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "The provided operation parameter was invalid",
            404: "The playback cannot be found",
            409: "The operation cannot be performed in the playback's current state",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None
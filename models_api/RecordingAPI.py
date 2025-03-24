from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class RecordingAPI(ResourceAPI):

    async def listStored(self, ):
        request_to="/recordings/stored"
        data = {}

        # TODO: implement listStored logic
        json_params = {}
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return [StoredRecording(**item) for item in response_data]

    async def getStored(self, recordingName: str, ):
        request_to="/recordings/stored/{recordingName}"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        data = {}

        # TODO: implement getStored logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Recording not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return StoredRecording(**response_data)

    async def deleteStored(self, recordingName: str, ):
        request_to="/recordings/stored/{recordingName}"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        data = {}

        # TODO: implement deleteStored logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Recording not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def getStoredFile(self, recordingName: str, ):
        request_to="/recordings/stored/{recordingName}/file"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        data = {}

        # TODO: implement getStoredFile logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            403: "The recording file could not be opened",
            404: "Recording not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return response_data

    async def copyStored(self, recordingName: str, destinationRecordingName: str, ):
        request_to="/recordings/stored/{recordingName}/copy"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        if not isinstance(destinationRecordingName, str):
            raise TypeError(f'destinationRecordingName must be str')

        data = {}

        # TODO: implement copyStored logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        data['destinationRecordingName']=destinationRecordingName
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Recording not found",
            409: "A recording with the same name already exists on the system",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return StoredRecording(**response_data)

    async def getLive(self, recordingName: str, ):
        request_to="/recordings/live/{recordingName}"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        data = {}

        # TODO: implement getLive logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Recording not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return LiveRecording(**response_data)

    async def cancel(self, recordingName: str, ):
        request_to="/recordings/live/{recordingName}"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        data = {}

        # TODO: implement cancel logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Recording not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def stop(self, recordingName: str, ):
        request_to="/recordings/live/{recordingName}/stop"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        data = {}

        # TODO: implement stop logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Recording not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def pause(self, recordingName: str, ):
        request_to="/recordings/live/{recordingName}/pause"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        data = {}

        # TODO: implement pause logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Recording not found",
            409: "Recording not in session",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def unpause(self, recordingName: str, ):
        request_to="/recordings/live/{recordingName}/pause"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        data = {}

        # TODO: implement unpause logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Recording not found",
            409: "Recording not in session",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def mute(self, recordingName: str, ):
        request_to="/recordings/live/{recordingName}/mute"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        data = {}

        # TODO: implement mute logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Recording not found",
            409: "Recording not in session",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def unmute(self, recordingName: str, ):
        request_to="/recordings/live/{recordingName}/mute"
        if not isinstance(recordingName, str):
            raise TypeError(f'recordingName must be str')

        data = {}

        # TODO: implement unmute logic
        json_params = {}
        request_to = request_to.replace('{recordingName}', str(recordingName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Recording not found",
            409: "Recording not in session",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None
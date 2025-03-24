from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class AsteriskAPI(ResourceAPI):

    async def getObject(self, configClass: str, objectType: str, id_: str, ):
        request_to="/asterisk/config/dynamic/{configClass}/{objectType}/{id}"
        if not isinstance(configClass, str):
            raise TypeError(f'configClass must be str')

        if not isinstance(objectType, str):
            raise TypeError(f'objectType must be str')

        if not isinstance(id_, str):
            raise TypeError(f'id_ must be str')

        data = {}

        # TODO: implement getObject logic
        json_params = {}
        request_to = request_to.replace('{configClass}', str(configClass))
        request_to = request_to.replace('{objectType}', str(objectType))
        request_to = request_to.replace('{id}', str(id_))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "{configClass|objectType|id} not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return [ConfigTuple(**item) for item in response_data]

    async def updateObject(self, configClass: str, objectType: str, id_: str, **kwargs):
        request_to="/asterisk/config/dynamic/{configClass}/{objectType}/{id}"
        if not isinstance(configClass, str):
            raise TypeError(f'configClass must be str')

        if not isinstance(objectType, str):
            raise TypeError(f'objectType must be str')

        if not isinstance(id_, str):
            raise TypeError(f'id_ must be str')

        data = {}

        optionals = {
             "fields": {"data_type": dict, "default": None},
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
        # TODO: implement updateObject logic
        json_params = {}
        request_to = request_to.replace('{configClass}', str(configClass))
        request_to = request_to.replace('{objectType}', str(objectType))
        request_to = request_to.replace('{id}', str(id_))
        fields = data.pop('fields', None)
        if fields:
            json_params.update(fields)
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.put(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Bad request body",
            403: "Could not create or update object",
            404: "{configClass|objectType} not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return [ConfigTuple(**item) for item in response_data]

    async def deleteObject(self, configClass: str, objectType: str, id_: str, ):
        request_to="/asterisk/config/dynamic/{configClass}/{objectType}/{id}"
        if not isinstance(configClass, str):
            raise TypeError(f'configClass must be str')

        if not isinstance(objectType, str):
            raise TypeError(f'objectType must be str')

        if not isinstance(id_, str):
            raise TypeError(f'id_ must be str')

        data = {}

        # TODO: implement deleteObject logic
        json_params = {}
        request_to = request_to.replace('{configClass}', str(configClass))
        request_to = request_to.replace('{objectType}', str(objectType))
        request_to = request_to.replace('{id}', str(id_))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            403: "Could not delete object",
            404: "{configClass|objectType|id} not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def getInfo(self, **kwargs):
        request_to="/asterisk/info"
        data = {}

        optionals = {
             "only": {"data_type": str, "default": "None"},
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
        # TODO: implement getInfo logic
        json_params = {}
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return AsteriskInfo(**response_data)

    async def ping(self, ):
        request_to="/asterisk/ping"
        data = {}

        # TODO: implement ping logic
        json_params = {}
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return AsteriskPing(**response_data)

    async def listModules(self, ):
        request_to="/asterisk/modules"
        data = {}

        # TODO: implement listModules logic
        json_params = {}
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return [Module(**item) for item in response_data]

    async def getModule(self, moduleName: str, ):
        request_to="/asterisk/modules/{moduleName}"
        if not isinstance(moduleName, str):
            raise TypeError(f'moduleName must be str')

        data = {}

        # TODO: implement getModule logic
        json_params = {}
        request_to = request_to.replace('{moduleName}', str(moduleName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Module could not be found in running modules.",
            409: "Module information could not be retrieved.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Module(**response_data)

    async def loadModule(self, moduleName: str, ):
        request_to="/asterisk/modules/{moduleName}"
        if not isinstance(moduleName, str):
            raise TypeError(f'moduleName must be str')

        data = {}

        # TODO: implement loadModule logic
        json_params = {}
        request_to = request_to.replace('{moduleName}', str(moduleName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            409: "Module could not be loaded.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def unloadModule(self, moduleName: str, ):
        request_to="/asterisk/modules/{moduleName}"
        if not isinstance(moduleName, str):
            raise TypeError(f'moduleName must be str')

        data = {}

        # TODO: implement unloadModule logic
        json_params = {}
        request_to = request_to.replace('{moduleName}', str(moduleName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Module not found in running modules.",
            409: "Module could not be unloaded.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def reloadModule(self, moduleName: str, ):
        request_to="/asterisk/modules/{moduleName}"
        if not isinstance(moduleName, str):
            raise TypeError(f'moduleName must be str')

        data = {}

        # TODO: implement reloadModule logic
        json_params = {}
        request_to = request_to.replace('{moduleName}', str(moduleName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.put(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Module not found in running modules.",
            409: "Module could not be reloaded.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def listLogChannels(self, ):
        request_to="/asterisk/logging"
        data = {}

        # TODO: implement listLogChannels logic
        json_params = {}
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return [LogChannel(**item) for item in response_data]

    async def addLog(self, logChannelName: str, configuration: str, ):
        request_to="/asterisk/logging/{logChannelName}"
        if not isinstance(logChannelName, str):
            raise TypeError(f'logChannelName must be str')

        if not isinstance(configuration, str):
            raise TypeError(f'configuration must be str')

        data = {}

        # TODO: implement addLog logic
        json_params = {}
        request_to = request_to.replace('{logChannelName}', str(logChannelName))
        data['configuration']=configuration
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Bad request body",
            409: "Log channel could not be created.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def deleteLog(self, logChannelName: str, ):
        request_to="/asterisk/logging/{logChannelName}"
        if not isinstance(logChannelName, str):
            raise TypeError(f'logChannelName must be str')

        data = {}

        # TODO: implement deleteLog logic
        json_params = {}
        request_to = request_to.replace('{logChannelName}', str(logChannelName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Log channel does not exist.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def rotateLog(self, logChannelName: str, ):
        request_to="/asterisk/logging/{logChannelName}/rotate"
        if not isinstance(logChannelName, str):
            raise TypeError(f'logChannelName must be str')

        data = {}

        # TODO: implement rotateLog logic
        json_params = {}
        request_to = request_to.replace('{logChannelName}', str(logChannelName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.put(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Log channel does not exist.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def getGlobalVar(self, variable: str, ):
        request_to="/asterisk/variable"
        if not isinstance(variable, str):
            raise TypeError(f'variable must be str')

        data = {}

        # TODO: implement getGlobalVar logic
        json_params = {}
        data['variable']=variable
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Missing variable parameter.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Variable(**response_data)

    async def setGlobalVar(self, variable: str, **kwargs):
        request_to="/asterisk/variable"
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
        # TODO: implement setGlobalVar logic
        json_params = {}
        data['variable']=variable
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.post(base_url+request_to, params=data, json_data=json_params)
        errors = {
            400: "Missing variable parameter.",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None
from .ResourceAPI import ResourceAPI
from .Response import Response

from ..errors.asterisk import *

from ..models.base_models import *


class MailboxesAPI(ResourceAPI):

    async def list(self, ):
        request_to="/mailboxes"
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
        return [Mailbox(**item) for item in response_data]

    async def get(self, mailboxName: str, ):
        request_to="/mailboxes/{mailboxName}"
        if not isinstance(mailboxName, str):
            raise TypeError(f'mailboxName must be str')

        data = {}

        # TODO: implement get logic
        json_params = {}
        request_to = request_to.replace('{mailboxName}', str(mailboxName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.get(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Mailbox not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        response_data = response.data
        return Mailbox(**response_data)

    async def update(self, mailboxName: str, oldMessages: int, newMessages: int, ):
        request_to="/mailboxes/{mailboxName}"
        if not isinstance(mailboxName, str):
            raise TypeError(f'mailboxName must be str')

        if not isinstance(oldMessages, int):
            raise TypeError(f'oldMessages must be int')

        if not isinstance(newMessages, int):
            raise TypeError(f'newMessages must be int')

        data = {}

        # TODO: implement update logic
        json_params = {}
        request_to = request_to.replace('{mailboxName}', str(mailboxName))
        data['oldMessages']=oldMessages
        data['newMessages']=newMessages
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.put(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Mailbox not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None

    async def delete(self, mailboxName: str, ):
        request_to="/mailboxes/{mailboxName}"
        if not isinstance(mailboxName, str):
            raise TypeError(f'mailboxName must be str')

        data = {}

        # TODO: implement delete logic
        json_params = {}
        request_to = request_to.replace('{mailboxName}', str(mailboxName))
        base_url = self.api_client.base_url.strip('/')
        response: Response = await self.api_client.delete(base_url+request_to, params=data, json_data=json_params)
        errors = {
            404: "Mailbox not found",
        }
        if response.status in errors:
            raise AsteriskError(response.status, errors[response.status])

        return None
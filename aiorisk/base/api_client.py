from abc import ABC, abstractclassmethod



class ApiClient(ABC):
    @abstractclassmethod
    async def get(self, path, **kwargs):
        pass

    @abstractclassmethod
    async def post(self, path, **kwargs):
        pass

    @abstractclassmethod
    async def delete(self, path, **kwargs):
        pass

    @abstractclassmethod
    async def put(self, path, **kwargs):
        pass

    @abstractclassmethod
    def base_url(self):
        pass
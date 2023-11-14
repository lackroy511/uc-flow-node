import json as python_json
from typing import Any, Dict

from uc_flow_nodes.schemas import NodeRunContext
from uc_http_requester.requester import Request, Response

from node.enums import TrashOperations
from util.dict_formatter import form_dict_to_request


class Trash:
    
    class RequestType:
        RESTORE = 'restore'
        
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/trash/resources/'
    BASE_DIR_OF_DISK = 'disk:/'
    
    def __init__(self, access_token: str) -> None:
        
        self.access_token: str = access_token
        self.base_headers: Dict[str, str] = {
            'Authorization': f'OAuth {self.access_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    async def empty_trash(
            self, params: Dict[str, Any]) -> Response:
        
        api_url: str = f'{self.BASE_URL}'   
        empty_trash: Request = Request(
            url=api_url,
            method=Request.Method.delete,
            headers=self.base_headers,
            params=params,
        )
        return await empty_trash.execute()

    async def get_trash_contents(
            self, params: Dict[str, Any]) -> Response:
        
        api_url: str = f'{self.BASE_URL}'   
        get_trash_contents: Request = Request(
            url=api_url,
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await get_trash_contents.execute()
        
        return response.json()
    
    async def restore_resource(
            self, params: Dict[str, Any]) -> Response:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.RESTORE}'   
        restore_resource: Request = Request(
            url=api_url,
            method=Request.Method.put,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await restore_resource.execute()
        
        return response.json()
    
    
class TrashProcess:
    
    def __init__(
            self, 
            operation: str, 
            trash: Trash, 
            properties: Dict[str, Any],
            json: NodeRunContext,
            ) -> None:
        
        self.json: NodeRunContext = json
        self.operation = operation
        self.trash = trash
        self.properties = properties
        
    async def execute(self) -> None:
        
        if self.operation == TrashOperations.empty_trash:
            await self.__empty_trash()
        
        if self.operation == TrashOperations.get_trash_contents:
            await self.__get_trash_contents()
        
        if self.operation == TrashOperations.restore_resource:
            await self.__restore_resource()
        
    async def __empty_trash(self) -> None:
        
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['empty_trash_params'],
        )
        response: Response = await self.trash.empty_trash(params)
        
        if response.status_code == 204:
            await self.json.save_result({'message': 'success'})
        else:
            await self.json.save_result(response.json())

    async def __get_trash_contents(self) -> None:
        
        path: str = self.properties['get_trash_contents_path']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['get_trash_contents_params'],
        )
        
        if params.get('path'):
            params['path'] = path
            
        response = await self.trash.get_trash_contents(params)
        
        await self.json.save_result(response)

    async def __restore_resource(self) -> None:
        
        path = self.properties['restore_resource_path']
        params = form_dict_to_request(
            self.properties['restore_resource_params'],
        )
        params['path'] = path
        response = await self.trash.restore_resource(params)
        
        await self.json.save_result(response)

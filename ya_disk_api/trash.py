import ujson
from typing import Any, Dict

from uc_flow_nodes.schemas import NodeRunContext
from uc_http_requester.requester import Request, Response

from node.enums import TrashOperations
from util.dict_formatter import form_dict_to_request
from ya_disk_api.yandex_disk_api import BaseYaDiskAPI


class Trash(BaseYaDiskAPI):
    
    class RequestType:
        RESTORE = 'restore'
        
    base_url = 'https://cloud-api.yandex.net/v1/disk/trash/resources/'

    async def empty_trash(
            self, params: Dict[str, Any]) -> Response:
        
        empty_trash: Request = await self.make_request(
            json=self.json,
            params=params,
            method=Request.Method.delete,
        )
        return empty_trash

    async def get_trash_contents(
            self, params: Dict[str, Any]) -> Response:
 
        get_trash_contents: Request = await self.make_request(
            json=self.json,
            params=params,
            method=Request.Method.get,
        )
        return ujson.loads(get_trash_contents['content'])
    
    async def restore_resource(
            self, params: Dict[str, Any]) -> Response:
           
        restore_resource: Request = await self.make_request(
            json=self.json,
            params=params,
            method=Request.Method.put,
            request_type=self.RequestType.RESTORE,
        )
        return ujson.loads(restore_resource['content'])

    
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
        
        if response['status_code'] == 204:
            await self.json.save_result({'message': 'success'})
        else:
            await self.json.save_result(ujson.loads(response['content']))

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

import json as python_json
from typing import Any, Dict

from uc_flow_nodes.schemas import NodeRunContext
from uc_http_requester.requester import Request, Response

from node.enums import (FilesAndFoldersOperations,
                        PublicFilesAndFoldersOperations, TrashOperations)
from util.dict_formatter import form_dict_to_request
from util.file_encoder import download_file


class Trash:
    
    class RequestType:
        RESTORE = 'restore'
        
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/trash/resources'
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
        response = await get_trash_contents.execute()
        
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
        
    async def execute(self):
        if self.operation == TrashOperations.empty_trash:
            await self.__empty_trash()
        
        if self.operation == TrashOperations.get_trash_contents:
            await self.__get_trash_contents()
        
    async def __empty_trash(self):
        params = form_dict_to_request(
            self.properties['empty_trash_params'])
        
        response = await self.trash.empty_trash(params)
        if response.status_code == 204:
            await self.json.save_result({'message': 'success'})
        else:
            await self.json.save_result(response.json())

    async def __get_trash_contents(self):
        params = form_dict_to_request(
            self.properties['get_trash_contents_params'])
        
        response = await self.trash.get_trash_contents(params)
        await self.json.save_result(response)

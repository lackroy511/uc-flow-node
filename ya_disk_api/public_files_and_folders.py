import json as python_json
from typing import Any, Dict

from uc_flow_nodes.schemas import NodeRunContext
from uc_http_requester.requester import Request, Response

from node.enums import (FilesAndFoldersOperations,
                        PublicFilesAndFoldersOperations)
from util.dict_formatter import form_dict_to_request
from util.file_encoder import download_file


class PublicFilesAndFolders:
    
    class RequestType:
        GET_DOWNLOAD_LINK = 'download'
        SAVE_RESOURCE = 'save-to-disk'
        
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/public/resources/'
    BASE_DIR_OF_DISK = 'disk:/'
    
    def __init__(self, access_token: str) -> None:
        
        self.access_token: str = access_token
        
        self.base_headers: Dict[str, str] = {
            'Authorization': f'OAuth {self.access_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    async def get_meta_info(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}'   
        meta_info: Request = Request(
            url=api_url,
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await meta_info.execute()
        
        return response.json()

    async def get_download_link(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.GET_DOWNLOAD_LINK}'   
        download_link: Request = Request(
            url=api_url,
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await download_link.execute()

        return response.json()
    
    async def save_resource(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.SAVE_RESOURCE}'   
        download_link: Request = Request(
            url=api_url,
            method=Request.Method.post,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await download_link.execute()

        return response.json()

    
class PublicFilesAndFoldersProcess:
    
    def __init__(
            self, 
            operation: str, 
            public_files_and_folders: PublicFilesAndFolders, 
            properties: Dict[str, Any],
            json: NodeRunContext,
            ) -> None:
        self.json: NodeRunContext = json
        self.operation = operation
        self.public_files_and_folders = public_files_and_folders
        self.properties = properties
        
    async def execute(self) -> None:
        if self.operation == PublicFilesAndFoldersOperations.get_meta_info:
            await self.__get_meta_info()
        
        if self.operation == PublicFilesAndFoldersOperations.get_download_link:
            await self.__get_download_link()
            
        if self.operation == PublicFilesAndFoldersOperations.save_resource:
            await self.__save_resource()
            
    async def __get_meta_info(self) -> None:
        
        public_key: str = self.properties['get_meta_info_public_key']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['get_public_meta_info_params'],
        )
        params['public_key'] = public_key
        
        response: Dict[str, Any] = \
            await self.public_files_and_folders.get_meta_info(
                params,
            )
        
        await self.json.save_result(response)

    async def __get_download_link(self) -> None:
        
        public_key: str = self.properties['get_download_link_public_key']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['get_download_link_params'],
        )
        params['public_key'] = public_key
        
        response: Dict[str, Any] = \
            await self.public_files_and_folders.get_download_link(
                params,
            )
        
        await self.json.save_result(response)

    async def __save_resource(self) -> None:
        
        public_key: str = self.properties['save_resource_public_key']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['save_resource_params'],
        )
        params['public_key'] = public_key
        
        response: Dict[str, Any] = \
            await self.public_files_and_folders.save_resource(
                params,
            )
        
        await self.json.save_result(response)

import ujson
from typing import Any, Dict

from uc_flow_nodes.schemas import NodeRunContext
from uc_http_requester.requester import Request, Response

from node.enums import (FilesAndFoldersOperations,
                        PublicFilesAndFoldersOperations)
from util.dict_formatter import form_dict_to_request
from util.file_encoder import download_file
from ya_disk_api.yandex_disk_api import BaseYaDiskAPI


class PublicFilesAndFolders(BaseYaDiskAPI):
    
    class RequestType:
        GET_DOWNLOAD_LINK = 'download'
        SAVE_RESOURCE = 'save-to-disk'
        
    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/'

    async def get_meta_info(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        meta_info: Request = await self.make_request(
            json=self.json,
            params=params,
            method=Request.Method.get,
        )
        return ujson.loads(meta_info['content'])

    async def get_download_link(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
           
        download_link: Request = await self.make_request(
            json=self.json,
            params=params,
            method=Request.Method.get,
            request_type=self.RequestType.GET_DOWNLOAD_LINK,
        )
        return ujson.loads(download_link['content'])
    
    async def save_resource(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
           
        save_resource: Request = await self.make_request(
            json=self.json,
            params=params,
            method=Request.Method.post,
            request_type=self.RequestType.SAVE_RESOURCE,
        )
        return ujson.loads(save_resource['content'])

    
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

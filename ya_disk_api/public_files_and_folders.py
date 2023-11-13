import json as python_json
from typing import Any, Dict

from uc_http_requester.requester import Request, Response

from uc_flow_nodes.schemas import NodeRunContext

from node.enums import FilesAndFoldersOperations, \
    PublicFilesAndFoldersOperations
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
        
    async def execute(self):
        if self.operation == PublicFilesAndFoldersOperations.get_meta_info:
            await self.__get_meta_info()
    
    async def __get_meta_info(self):
        public_key = self.properties['get_meta_info_public_key']
        params = form_dict_to_request(
            self.properties['get_public_meta_info_params'])
        params['public_key'] = public_key
        
        meta_info = await self.public_files_and_folders.get_meta_info(params)
        
        await self.json.save_result(meta_info)

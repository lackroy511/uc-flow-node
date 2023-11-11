import json as python_json
from typing import Any, Dict

from uc_http_requester.requester import Request

from uc_flow_nodes.schemas import NodeRunContext

from node.enums import FilesAndFoldersOperations
from util.dict_formatter import form_dict_to_request


class FilesAndFolders:
    
    class RequestType:
        UPLOAD_TO_DISK = 'upload'
        GET_FLAT_LIST = 'files'
    
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources/'
    BASE_DIR_OF_DISK = 'disk:/'
    
    def __init__(self, access_token: str) -> None:
        
        self.access_token: str = access_token
        
        self.base_headers: Dict[str, str] = {
            'Authorization': f'OAuth {self.access_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
    
    async def del_file_or_folder(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}'   
        
        delete: Request = Request(
            url=api_url,
            method=Request.Method.delete,
            headers=self.base_headers,
            params=params,
        )
        return await delete.execute()
    
    async def get_meta_info(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}'   
        
        meta_info: Request = Request(
            url=api_url,
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response = await meta_info.execute()

        return response.json()
    
    async def update_meta_info(
            self, 
            params: Dict[str, Any], 
            body: Dict[str, str]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}'   
        
        meta_info: Request = Request(
            url=api_url,
            method=Request.Method.patch,
            headers=self.base_headers,
            params=params,
            data=python_json.dumps(body),
        )
        response = await meta_info.execute()

        return response.json()
    
    async def create_folder(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}'   
        
        create_folder: Request = Request(
            url=api_url,
            method=Request.Method.put,
            headers=self.base_headers,
            params=params,
        )
        response = await create_folder.execute()

        return response.json()
    
    async def upload_from_inet_to_disk(
            self, 
            download_link: str,
            file_name: str) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.UPLOAD_TO_DISK}'   
        params: Dict[str, str] = {
            'url': download_link,
            'path': self.BASE_DIR_OF_DISK + file_name,
        }
        
        upload_file: Request = Request(
            url=api_url,
            method=Request.Method.post,
            headers=self.base_headers,
            params=params,
        )
        response = await upload_file.execute()
        
        return response.json()

    async def get_flat_list(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.GET_FLAT_LIST}'   
        
        flat_list: Request = Request(
            url=api_url,
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response = await flat_list.execute()
        
        return response.json()


class FilesAndFoldersProcess:
    
    def __init__(
            self, 
            operation: str, 
            files_and_folders: FilesAndFolders, 
            properties: Dict[str, Any],
            json: NodeRunContext,
            ) -> None:
        
        self.json: NodeRunContext = json
        self.operation = operation
        self.files_and_folders = files_and_folders
        self.properties = properties
    
    async def execute(self):
        if self.operation == FilesAndFoldersOperations.del_file_or_folder:
            await self.__del_file_or_folder()
        
        if self.operation == FilesAndFoldersOperations.get_meta_info:
            await self.__get_meta_info()
        
        if self.operation == FilesAndFoldersOperations.update_meta_info:
            await self.__update_meta_info()
        
        if self.operation == FilesAndFoldersOperations.create_folder:
            await self.__create_folder()
            
        if self.operation == FilesAndFoldersOperations.upload_file:
            await self.__upload_file()
        
        if self.operation == FilesAndFoldersOperations.get_flat_list:
            await self.__get_flat_list()
    
    async def __del_file_or_folder(self) -> None:
        
        path = self.properties['path_to_delete']
        params = form_dict_to_request(self.properties['delete_params'])
        params['path'] = path
        
        response = await self.files_and_folders.del_file_or_folder(
            params)
        
        if response.status_code == 204:
            await self.json.save_result({'message': 'success'})
        else:
            await self.json.save_result(response.json())
    
    async def __get_meta_info(self) -> None:
        
        path = self.properties['get_meta_info_path']
        params = form_dict_to_request(
            self.properties['get_meta_info_params'])
        params['path'] = path

        response = await self.files_and_folders.get_meta_info(
            params)
        
        await self.json.save_result(response)
    
    async def __update_meta_info(self) -> None:
        
        path = self.properties['update_meta_info_path']
        params = form_dict_to_request(
            self.properties['update_meta_info_params'])
        params['path'] = path
        body = self.properties['body']
        
        response = await self.files_and_folders.update_meta_info(
            params=params, body=body,
        )
        await self.json.save_result(response)

    async def __create_folder(self) -> None:
        
        path = self.properties['create_folder_path']
        params = form_dict_to_request(
            self.properties['create_folder_params'])
        params['path'] = path
        
        response = await self.files_and_folders.create_folder(params)
        await self.json.save_result(response)
    
    async def __upload_file(self) -> None:
        
        download_link: str = self.properties['download_link']
        file_name: str = self.properties['file_name']
        
        response = \
            await self.files_and_folders.upload_from_inet_to_disk(
                download_link, file_name)
        await self.json.save_result(response)
    
    async def __get_flat_list(self) -> None:
        
        params = form_dict_to_request(
            self.properties['get_flat_list_params'])
        flat_list = await self.files_and_folders.get_flat_list(params)

        await self.json.save_result(flat_list)

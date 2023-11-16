import json as python_json
from typing import Any, Dict

from uc_flow_nodes.schemas import NodeRunContext
from uc_http_requester.requester import Request, Response

from node.enums import FilesAndFoldersOperations
from util.dict_formatter import form_dict_to_request
from util.file_encoder import download_file


class FilesAndFolders:
    
    class RequestType:
        UPLOAD_TO_DISK = 'upload'
        GET_FLAT_LIST = 'files'
        COPY_FILE_OR_FOLDER = 'copy'
        GET_FILE_IN_BASE64 = 'download'
        GET_FLAT_LIST_ORDER_BY_DATE = 'last-uploaded'
        MOVE_FILE_OR_FOLDER = 'move'
        GET_PUBLIC_RESOURCE_LIST = 'public'
        PUBLISH_RESOURCE = 'publish'
        UNPUBLISH_RESOURCE = 'unpublish'
        GET_UPLOAD_LINK = 'upload'
    
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
        response: Response = await meta_info.execute()

        return response.json()
    
    async def update_meta_info(
            self, 
            params: Dict[str, Any], 
            body: Dict[str, str]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}'   
        update_meta_info: Request = Request(
            url=api_url,
            method=Request.Method.patch,
            headers=self.base_headers,
            params=params,
            data=python_json.dumps(body),
        )
        response: Response = await update_meta_info.execute()

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
        response: Response = await create_folder.execute()

        return response.json()
    
    async def copy_file_or_folder(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.COPY_FILE_OR_FOLDER}'      
        copy: Request = Request(
            url=api_url,
            method=Request.Method.post,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await copy.execute()

        return response.json()
    
    async def get_file_in_base64(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.GET_FILE_IN_BASE64}'      
        get_file: Request = Request(
            url=api_url,
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await get_file.execute()

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
        response: Response = await flat_list.execute()
        
        return response.json()
    
    async def get_flat_list_ordered_by_date(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}' + \
                       f'{self.RequestType.GET_FLAT_LIST_ORDER_BY_DATE}'   
        flat_list: Request = Request(
            url=api_url,
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await flat_list.execute()
        
        return response.json()
    
    async def move_file_or_folder(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.MOVE_FILE_OR_FOLDER}'      
        move_file: Request = Request(
            url=api_url,
            method=Request.Method.post,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await move_file.execute()

        return response.json()
    
    async def get_public_resource_list(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}' + \
                       f'{self.RequestType.GET_PUBLIC_RESOURCE_LIST}'   
        public_resource_list: Request = Request(
            url=api_url,
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await public_resource_list.execute()
        
        return response.json()
    
    async def publish_resource(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.PUBLISH_RESOURCE}'      
        publish: Request = Request(
            url=api_url,
            method=Request.Method.put,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await publish.execute()

        return response.json()
    
    async def unpublish_resource(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.UNPUBLISH_RESOURCE}'      
        unpublish: Request = Request(
            url=api_url,
            method=Request.Method.put,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await unpublish.execute()

        return response.json()
    
    async def get_upload_link(
            self, params: Dict[str, Any]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.GET_UPLOAD_LINK}'      
        get_upload_link: Request = Request(
            url=api_url,
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await get_upload_link.execute()

        return response.json()
    
    async def upload_from_inet_to_disk(
            self, 
            download_link: str,
            file_name: str) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}{self.RequestType.UPLOAD_TO_DISK}'   
        params: Dict[str, str] = {
            'url': download_link,
            'path': file_name,
        }
        upload_file: Request = Request(
            url=api_url,
            method=Request.Method.post,
            headers=self.base_headers,
            params=params,
        )
        response: Response = await upload_file.execute()
        
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
    
    async def execute(self) -> None:
        if self.operation == FilesAndFoldersOperations.del_file_or_folder:
            await self.__del_file_or_folder()
        
        if self.operation == FilesAndFoldersOperations.get_meta_info:
            await self.__get_meta_info()
        
        if self.operation == FilesAndFoldersOperations.update_meta_info:
            await self.__update_meta_info()
        
        if self.operation == FilesAndFoldersOperations.create_folder:
            await self.__create_folder()
        
        if self.operation == FilesAndFoldersOperations.copy_file_or_folder:
            await self.__copy_file_or_folder()
        
        if self.operation == FilesAndFoldersOperations.get_file_in_base64:
            await self.__get_file_in_base64()
        
        if self.operation == FilesAndFoldersOperations.get_flat_list:
            await self.__get_flat_list()
        
        if self.operation == \
                FilesAndFoldersOperations.get_flat_list_ordered_by_date:
            await self.__get_flat_list_ordered_by_date()
        
        if self.operation == FilesAndFoldersOperations.move_file_or_folder:
            await self.__move_file_or_folder()
        
        if self.operation == \
                FilesAndFoldersOperations.get_public_resource_list:
            await self.__get_public_resource_list()
        
        if self.operation == FilesAndFoldersOperations.publish_resource:
            await self.__publish_resource()
        
        if self.operation == FilesAndFoldersOperations.unpublish_resource:
            await self.__unpublish_resource()
        
        if self.operation == FilesAndFoldersOperations.get_upload_link:
            await self.__get_upload_link()
        
        if self.operation == FilesAndFoldersOperations.upload_file:
            await self.__upload_file()
    
    async def __del_file_or_folder(self) -> None:
        
        path: str = self.properties['path_to_delete']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['delete_params'],
        )
        params['path'] = path
        
        response: Response = await self.files_and_folders.del_file_or_folder(
            params,
        )
        
        if response.status_code == 204:
            await self.json.save_result({'message': 'success'})
        else:
            await self.json.save_result(response.json())
    
    async def __get_meta_info(self) -> None:
        
        path: str = self.properties['get_meta_info_path']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['get_meta_info_params'],
        )
        params['path'] = path

        response: Response = await self.files_and_folders.get_meta_info(
            params,
        )
        
        await self.json.save_result(response)
    
    async def __update_meta_info(self) -> None:
        
        path: str = self.properties['update_meta_info_path']
        body: Dict[str, Any] = self.properties['body']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['update_meta_info_params'],
        )
        params['path'] = path
        
        response: Response = await self.files_and_folders.update_meta_info(
            params=params, 
            body=body,
        )
        await self.json.save_result(response)

    async def __create_folder(self) -> None:
        
        path: str = self.properties['create_folder_path']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['create_folder_params'],
        )
        params['path'] = path
        
        response: Response = await self.files_and_folders.create_folder(
            params,
        )
        await self.json.save_result(response)
    
    async def __copy_file_or_folder(self) -> None:
        
        path_from: str = self.properties['copy_from_path']
        path_to: str = self.properties['copy_to_path']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['copy_file_or_folder_params'],
        )
        params['from'] = path_from
        params['path'] = path_to
        
        response = await self.files_and_folders.copy_file_or_folder(
            params,
        )
        await self.json.save_result(response)
    
    async def __get_file_in_base64(self) -> None:
        
        path: str = self.properties['get_file_in_base64_path']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['get_file_in_base64_params'],
        )
        params['path'] = path
        
        response: Response = await self.files_and_folders.get_file_in_base64(
            params,
        )
        
        if response.get('href'):
            url = response.get('href')
            file_in_base64 = await download_file(url)
            await self.json.save_result(file_in_base64)
        else:
            await self.json.save_result(response)
    
    async def __get_flat_list(self) -> None:
        
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['get_flat_list_params'],
        )
        flat_list: Dict[str, Any] = await self.files_and_folders.get_flat_list(
            params,
        )

        await self.json.save_result(flat_list)
        
    async def __get_flat_list_ordered_by_date(self) -> None:
        
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['get_flat_list_ordered_by_date_params'],
        )
        flat_list: Dict[str, Any] = \
            await self.files_and_folders.get_flat_list_ordered_by_date(
                params,
            )

        await self.json.save_result(flat_list)
    
    async def __move_file_or_folder(self) -> None:
        
        path_from: str = self.properties['move_from_path']
        path_to: str = self.properties['move_to_path']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['move_file_or_folder_params'],
        )
        params['from'] = path_from
        params['path'] = path_to
        
        response: Response = await self.files_and_folders.move_file_or_folder(
            params,
        )
        await self.json.save_result(response)
    
    async def __get_public_resource_list(self) -> None:
        
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['get_public_resource_list_params'],
        )
        resource_list: Dict[str, Any] = \
            await self.files_and_folders.get_public_resource_list(
                params,
            )

        await self.json.save_result(resource_list)
    
    async def __publish_resource(self) -> None:
        
        path: str = self.properties['publish_resource_path']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['publish_resource_params'],
        )
        params['path'] = path
        
        response: Response = await self.files_and_folders.publish_resource(
            params,
        )
        await self.json.save_result(response)
        
    async def __unpublish_resource(self) -> None:
        
        path: str = self.properties['unpublish_resource_path']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['unpublish_resource_params'],
        )
        params['path'] = path
        
        response: Response = await self.files_and_folders.unpublish_resource(
            params,
        )
        await self.json.save_result(response)
    
    async def __get_upload_link(self) -> None:
        
        path: str = self.properties['get_upload_link_path']
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['get_upload_link_params'],
        )
        params['path'] = path
        
        response: Response = await self.files_and_folders.get_upload_link(
            params,
        )
        await self.json.save_result(response)
    
    async def __upload_file(self) -> None:
        
        download_link: str = self.properties['download_link']
        file_name: str = self.properties['file_name']
        
        response: Response = \
            await self.files_and_folders.upload_from_inet_to_disk(
                download_link, 
                file_name,
            )
        await self.json.save_result(response)

from uc_http_requester.requester import Request

from typing import Any, Dict

import json


class YaDiskApi:
    
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
            'Content-Type': 'application/json'
        }
 
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

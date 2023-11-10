
from typing import Any, Dict

from uc_http_requester.requester import Request


class UserDisk:
    
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/'
    
    def __init__(self, access_token: str) -> None:
        
        self.access_token: str = access_token
        
        self.base_headers: Dict[str, str] = {
            'Authorization': f'OAuth {self.access_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
    
    async def get_meta_info(
            self, params: Dict[str, str]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}'   
        
        flat_list: Request = Request(
            url=api_url,
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response = await flat_list.execute()
        
        return response.json()

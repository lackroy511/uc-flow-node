import ujson
from typing import Any, Dict

from uc_flow_nodes.schemas import NodeRunContext
from uc_http_requester.requester import Request, Response

from node.enums import UserDiskOptions
from util.dict_formatter import form_dict_to_request
from ya_disk_api.yandex_disk_api import BaseYaDiskAPI


class UserDisk(BaseYaDiskAPI):
    
    base_url = 'https://cloud-api.yandex.net/v1/disk/'
    
    async def get_meta_info(
            self, 
            params: Dict[str, str]) -> Dict[str, Any]:
  
        meta_info: Response = await self.make_request(
            self.json,
            params,
        )
        
        return ujson.loads(meta_info['content'])


class UserDiskProcess:
    
    def __init__(
            self, 
            operation: str, 
            user_disk: UserDisk, 
            properties: Dict[str, Any],
            json: NodeRunContext,
            ) -> None:
        
        self.json: NodeRunContext = json
        self.operation = operation
        self.user_disk = user_disk
        self.properties = properties
        
    async def execute(self) -> None:
        
        if self.operation == UserDiskOptions.get_meta_info:
            await self.__get_meta_info()
    
    async def __get_meta_info(self) -> None:
        
        params: Dict[str, Any] = form_dict_to_request(
            self.properties['user_disk_params'],
        )
        meta_info: Dict[str, Any] = await self.user_disk.get_meta_info(
            params,
        )
        
        await self.json.save_result(meta_info)

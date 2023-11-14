from typing import Any, Dict

from uc_flow_nodes.schemas import NodeRunContext
from uc_http_requester.requester import Request

from node.enums import AsyncOpOperations
from util.dict_formatter import form_dict_to_request


class AsyncOperation:
    
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/operations/'
    
    def __init__(self, access_token: str) -> None:
        
        self.access_token: str = access_token
        
        self.base_headers: Dict[str, str] = {
            'Authorization': f'OAuth {self.access_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
    
    async def get_operation_status(
            self, 
            operation_id: str,
            params: Dict[str, str]) -> Dict[str, Any]:
        
        api_url: str = f'{self.BASE_URL}'   
        
        get_operation_status: Request = Request(
            url=api_url + (operation_id if operation_id else ''),
            method=Request.Method.get,
            headers=self.base_headers,
            params=params,
        )
        response = await get_operation_status.execute()
        return response.json()


class AsyncOperationProcess:
    
    def __init__(
            self, 
            operation: str, 
            async_operation: AsyncOperation, 
            properties: Dict[str, Any],
            json: NodeRunContext,
            ) -> None:
        
        self.json: NodeRunContext = json
        self.operation = operation
        self.async_operation = async_operation
        self.properties = properties
        
    async def execute(self) -> None:
        if self.operation == AsyncOpOperations.get_operation_status:
            await self.__get_operation_status()
    
    async def __get_operation_status(self) -> None:
        operation_id = self.properties['operation_id']
        params = form_dict_to_request(
            self.properties['get_operation_status_params'])
        status = await self.async_operation.get_operation_status(
            operation_id, params)
        
        await self.json.save_result(status)

from typing import Dict
import json as python_json
from uc_http_requester.requester import Request, Response
from uc_flow_nodes.schemas import NodeRunContext


class BaseYaDiskAPI:
    
    base_url = None
    base_headers: Dict[str, str] = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    
    def __init__(self, json: NodeRunContext) -> None:
        self.json = json
    
    async def make_request(
            self,
            json: NodeRunContext,
            params: Dict[str, str],
            method: str,
            headers: Dict[str, str] = None,
            data: Dict[str, str] = None,
            request_type: str = None,
            operation_id: str = None) -> Response:
        
        api_url = self.__get_api_url(request_type, operation_id)
        
        response: Response = await json.requester.request(
            Request(
                url=api_url,
                headers=self.base_headers if headers is None else headers,
                data=python_json.dumps(data) if data else {},
                method=method,
                params=params,
                auth=json.credential_id,
            ),
        )
        
        return response

    def __get_api_url(
            self, 
            request_type: str = None,
            operation_id: str = None) -> str:
        
        api_url = self.base_url
        
        if request_type:
            api_url: str = f'{self.base_url}' + \
                           f'{request_type if request_type else ""}' 
        elif operation_id:
            api_url: str = f'{self.base_url}' + \
                           f'{operation_id if operation_id else ""}'
        
        return api_url

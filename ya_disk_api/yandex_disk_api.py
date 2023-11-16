from typing import Dict
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
            request_type: str = None,
            operation_id: str = None) -> Response:
        
        if request_type:
            api_url: str = f'{self.base_url}' + \
                           f'{request_type if request_type else ""}' 
        elif operation_id:
            api_url: str = f'{self.base_url}' + \
                           f'{operation_id if operation_id else ""}'                    
          
        response: Response = await json.requester.request(
            Request(
                url=api_url,
                headers=self.base_headers,
                method=Request.Method.get,
                params=params,
                auth=json.credential_id,
            ),
        )
        
        return response

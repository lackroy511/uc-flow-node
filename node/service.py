from typing import List, Tuple


from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import execute, info
from uc_flow_schemas import flow
from uc_flow_schemas.flow import NodeType as BaseNodeType
from uc_flow_schemas.flow import RunState
from uc_http_requester.requester import Request
from node.credential_type import CredentialType

from node.node_type import NodeType

from ya_disk_api.main_process import MainProcess


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType
        credential_types: Tuple[CredentialType] = (CredentialType(),) 


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        
        try:
            properties = json.node.data.properties
            resource = properties['resource']

            ya_disk_token = None
            
            main_process = MainProcess(
                ya_disk_token,
                resource,
                properties,
                json,
            )
            await main_process.execute()
            
            json.state = RunState.complete
                
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error

        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView

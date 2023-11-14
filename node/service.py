from typing import List

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import execute, info
from uc_flow_schemas import flow
from uc_flow_schemas.flow import NodeType as BaseNodeType
from uc_flow_schemas.flow import RunState
from uc_http_requester.requester import Request

from node.node_type import NodeType

from ya_disk_api.main_process import MainProcess


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        properties = json.node.data.properties
        try:
            ya_disk_token = properties['api_token']
            resource = properties['resource']
            
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

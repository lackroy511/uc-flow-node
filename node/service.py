from typing import List

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import execute, info
from uc_flow_schemas import flow
from uc_flow_schemas.flow import CredentialProtocol, Defaults, DisplayOptions
from uc_flow_schemas.flow import NodeType as BaseNodeType
from uc_flow_schemas.flow import OptionValue, Property, RunState
from uc_http_requester.requester import Request

from api.ya_disk_api import YaDiskApi
from node.enums import MediaTypes, Operations, Params, PreviewSizes
from node.node_type import NodeType
from util.dict_formatter import form_dict_to_request


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        properties = json.node.data.properties
        try:
            ya_disk_token = properties['api_token']
            operation = properties['operation']
            ya_disk_api = YaDiskApi(ya_disk_token)
            
            if operation == Operations.upload_file:
                download_link: str = properties['download_link']
                file_name: str = properties['file_name']
                
                response = await ya_disk_api.upload_from_inet_to_disk(
                    download_link, file_name)
                await json.save_result({'result': response})
            
            if operation == Operations.get_flat_list:
                params = form_dict_to_request(properties['params'])
                flat_list = await ya_disk_api.get_flat_list(params)

                await json.save_result({'result': flat_list})
            
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

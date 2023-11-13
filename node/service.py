from typing import List

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import execute, info
from uc_flow_schemas import flow
from uc_flow_schemas.flow import CredentialProtocol, Defaults, DisplayOptions
from uc_flow_schemas.flow import NodeType as BaseNodeType
from uc_flow_schemas.flow import OptionValue, Property, RunState
from uc_http_requester.requester import Request

from node.enums import (FilesAndFoldersOperations, MediaTypes, Params,
                        PreviewSizes, Resources, UserDiskOptions)
from node.node_type import NodeType
from util.dict_formatter import form_dict_to_request
from util.path_encoder import encode_path_to_url_format
from ya_disk_api.async_operation import AsyncOperation, AsyncOperationProcess
from ya_disk_api.files_and_folders import (FilesAndFolders,
                                           FilesAndFoldersProcess)
from ya_disk_api.public_files_and_folders import (PublicFilesAndFolders,
                                                  PublicFilesAndFoldersProcess)
from ya_disk_api.trash import Trash, TrashProcess
from ya_disk_api.user_disk import UserDisk, UserDiskProcess


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        properties = json.node.data.properties
        try:
            ya_disk_token = properties['api_token']
            resource = properties['resource']
            
            if resource == Resources.user_disk:
                user_disk = UserDisk(ya_disk_token)
                operation = properties['user_disk_operations']
                
                process = UserDiskProcess(
                    operation, user_disk, properties, json)
                await process.execute()
                
            if resource == Resources.files_and_folders:
                files_and_folders = FilesAndFolders(ya_disk_token)
                operation = properties['files_and_folders_operations']
                
                process = FilesAndFoldersProcess(
                    operation, files_and_folders, properties, json)
                await process.execute()
            
            if resource == Resources.public_files_and_folders:
                public_files_and_folders = PublicFilesAndFolders(ya_disk_token)
                operation = properties['public_files_and_folders_operations']
                
                process = PublicFilesAndFoldersProcess(
                    operation, public_files_and_folders, properties, json)
                await process.execute()
            
            if resource == Resources.trash:
                trash = Trash(ya_disk_token)
                operation = properties['trash_operations']
                
                process = TrashProcess(
                    operation, trash, properties, json)
                await process.execute()
            
            if resource == Resources.async_operation:
                async_operation = AsyncOperation(ya_disk_token)
                operation = properties['async_operation_operations']
                
                process = AsyncOperationProcess(
                    operation, async_operation, properties, json)
                await process.execute()
            
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

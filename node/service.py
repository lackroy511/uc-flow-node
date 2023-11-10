from typing import List

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import execute, info
from uc_flow_schemas import flow
from uc_flow_schemas.flow import CredentialProtocol, Defaults, DisplayOptions
from uc_flow_schemas.flow import NodeType as BaseNodeType
from uc_flow_schemas.flow import OptionValue, Property, RunState
from uc_http_requester.requester import Request
from util.path_encoder import encode_path_to_url_format

from ya_disk_api.files_and_folders import FilesAndFolders
from node.enums import MediaTypes, FilesAndFoldersOperations, \
    Params, PreviewSizes, Resources
from node.node_type import NodeType
from util.dict_formatter import form_dict_to_request
from ya_disk_api.user_disk import UserDisk


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
                params = form_dict_to_request(properties['user_disk_params'])
                
                meta_info = await user_disk.get_meta_info(params)
                
                await json.save_result(meta_info)
                
            if resource == Resources.files_and_folders:
                operation = properties['files_and_folders_operations']
                files_and_folders = FilesAndFolders(ya_disk_token)
                
                if operation == FilesAndFoldersOperations.del_file_or_folder:
                    path = properties['path_to_delete']
                    params = form_dict_to_request(properties['delete_params'])
                    params['path'] = path
                    
                    response = await files_and_folders.del_file_or_folder(
                        params)
                    
                    if response.status_code == 204:
                        await json.save_result({'message': 'success'})
                    else:
                        await json.save_result(response.json())
                
                if operation == FilesAndFoldersOperations.get_meta_info:
                    path = properties['get_meta_info_path']
                    params = form_dict_to_request(
                        properties['get_meta_info_params'])
                    params['path'] = path

                    response = await files_and_folders.get_meta_info(
                        params)
                    
                    await json.save_result(response)
                
                if operation == FilesAndFoldersOperations.update_meta_info:
                    path = properties['update_meta_info_path']
                    params = form_dict_to_request(
                        properties['update_meta_info_params'])
                    params['path'] = path
                    body = properties['body']
                    
                    response = await files_and_folders.update_meta_info(
                        params=params, body=body,
                    )
                    await json.save_result(response)
                    
                if operation == FilesAndFoldersOperations.upload_file:
                    download_link: str = properties['download_link']
                    file_name: str = properties['file_name']
                    
                    response = \
                        await files_and_folders.upload_from_inet_to_disk(
                            download_link, file_name)
                    await json.save_result(response)
                
                if operation == FilesAndFoldersOperations.get_flat_list:
                    params = form_dict_to_request(properties['params'])
                    flat_list = await files_and_folders.get_flat_list(params)

                    await json.save_result(flat_list)
            
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

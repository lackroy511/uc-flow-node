from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import CredentialProtocol, Defaults, DisplayOptions
from uc_flow_schemas.flow import NodeType as BaseNodeType
from uc_flow_schemas.flow import OptionValue, Property, RunState

from node.enums import CreateFolderParams, DelFileOrFolderParams, \
    GetMetaInfoParams, MediaTypes, \
    FilesAndFoldersOperations, Params, \
    PreviewSizes, Resources, UpdateMetaInfoParams, UserDiskOptions

from node.properties.params import property_get_flat_list_params, \
    property_user_disk_params, property_delete_params, \
    property_get_meta_info_params, property_update_meta_info_params, \
    property_create_folder_params, property_copy_file_or_folder_params, \
    property_get_file_in_base64_params, \
    property_get_flat_list_ordered_by_date_params, \
    property_move_file_or_folder_params, \
    property_get_public_resource_list_params, \
    property_publish_resource_params, property_unpublish_resource_params, \
    property_get_upload_link_params

from node.properties.operations import property_user_disk_operations, \
    property_files_and_folders_operations


from node.properties.paths import property_path_to_delete, \
    property_get_meta_info_path, property_update_meta_info_path, \
    property_create_folder_path, property_copy_from_path, \
    property_copy_to_path, property_get_file_in_base64_path, \
    property_move_from_path, property_move_to_path, \
    property_publish_resource_path, property_unpublish_resource_path, \
    property_get_upload_link_path
    
from node.properties.unique import property_body, property_download_link, \
    property_file_name


class NodeType(flow.NodeType):
    id: str = 'ee1acfd5-ff91-49ec-92fd-072fb39b61ce'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'my_service'
    displayName: str = 'my_service'
    icon: str = '<svg><text x="8" y="50" font-size="50">🦥</text></svg>'
    description: str = 'my_service'
    properties: List[Property] = [
        Property(
            displayName='API token',
            name='api_token',
            type=Property.Type.STRING,
            required=True,
            default='',
            description='Токен доступа к апи Ядиска',
        ),
        
        Property(
            displayName='Resource',
            name='resource',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='User disk',
                    value=Resources.user_disk,
                ),
                OptionValue(
                    name='Files and folders',
                    value=Resources.files_and_folders,
                ),
            ],
        ),
        
        # user disk
        property_user_disk_operations,
        # user disk\get meta info
        property_user_disk_params,
        
        # files and folders\operations
        property_files_and_folders_operations,

        # files and folders\delete file or folder
        property_path_to_delete,
        property_delete_params,
        
        # files and folders\get meta info
        property_get_meta_info_path,
        property_get_meta_info_params,
        
        # files and folders\update meta info
        property_update_meta_info_path,
        property_body,
        property_update_meta_info_params,
        
        # files and folders\create folder
        property_create_folder_path,
        property_create_folder_params,
        
        # files and folders\copy file or folder
        property_copy_from_path,
        property_copy_to_path,
        property_copy_file_or_folder_params,
        
        # files and folders\get the file in base64
        property_get_file_in_base64_path,
        property_get_file_in_base64_params,
        
        # files and folders\get flat list
        property_get_flat_list_params,
        
        # files and folders\get flat list ordered by download date
        property_get_flat_list_ordered_by_date_params,
        
        # files and folders\move file or folder
        property_move_from_path,
        property_move_to_path,
        property_move_file_or_folder_params,
        
        # files and folders\get public resource list
        property_get_public_resource_list_params,
        
        # files and folders\Publish resource
        property_publish_resource_path,
        property_publish_resource_params,
        
        # files and folders\Unpublish resource
        property_unpublish_resource_path,
        property_unpublish_resource_params,
        
        # files and folders\get upload link
        property_get_upload_link_path,
        property_get_upload_link_params,
        
        # files and folders\upload file
        property_download_link,
        property_file_name,
    ]

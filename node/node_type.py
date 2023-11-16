from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import CredentialProtocol, Defaults, DisplayOptions
from uc_flow_schemas.flow import NodeType as BaseNodeType
from uc_flow_schemas.flow import OptionValue, Property, RunState

from node.enums import Resources
from node.properties.operations import (
    property_async_operation_options, property_files_and_folders_operations,
    property_public_files_and_folders_operations, property_trash_operations,
    property_user_disk_operations)
from node.properties.params import (
    property_copy_file_or_folder_params, property_create_folder_params,
    property_delete_params, property_empty_trash_params,
    property_get_download_link_params, property_get_file_in_base64_params,
    property_get_flat_list_ordered_by_date_params,
    property_get_flat_list_params, property_get_meta_info_params,
    property_get_operation_status_params, property_get_public_meta_info_params,
    property_get_public_resource_list_params,
    property_get_trash_contents_params, property_get_upload_link_params,
    property_move_file_or_folder_params, property_publish_resource_params,
    property_restore_resource_params, property_save_resource_params,
    property_unpublish_resource_params, property_update_meta_info_params,
    property_user_disk_params)
from node.properties.paths import (property_copy_from_path,
                                   property_copy_to_path,
                                   property_create_folder_path,
                                   property_get_file_in_base64_path,
                                   property_get_meta_info_path,
                                   property_get_trash_contents_path,
                                   property_get_upload_link_path,
                                   property_move_from_path,
                                   property_move_to_path,
                                   property_path_to_delete,
                                   property_publish_resource_path,
                                   property_restore_resource_path,
                                   property_unpublish_resource_path,
                                   property_update_meta_info_path)
from node.properties.public_keys import (property_get_download_link_public_key,
                                         property_get_meta_info_public_key,
                                         property_save_resource_public_key)
from node.properties.unique import (property_body, property_download_link,
                                    property_file_name, property_operation_id)
from static.icon import ICON


class NodeType(flow.NodeType):
    id: str = 'ee1acfd5-ff91-49ec-92fd-072fb39b61ce'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'yandex_disk_api'
    displayName: str = 'Yandex Disk API'
    icon: str = ICON
    description: str = 'Yandex Disk API'
    properties: List[Property] = [
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
                OptionValue(
                    name='Public files and folders',
                    value=Resources.public_files_and_folders,
                ),
                OptionValue(
                    name='Trash',
                    value=Resources.trash,
                ),
                OptionValue(
                    name='Async operation',
                    value=Resources.async_operation,
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
        
        # public files and folders\operations
        property_public_files_and_folders_operations,
        
        # public files and folders\get meta info
        property_get_meta_info_public_key,
        property_get_public_meta_info_params,
        
        # public files and folders\get download link
        property_get_download_link_public_key,
        property_get_download_link_params,
        
        # public files and folders\save resource to download folder
        property_save_resource_public_key,
        property_save_resource_params,
        
        # trash\operations
        property_trash_operations,
        
        # trash\empty trash
        property_empty_trash_params,
        
        # trash\get trash contents
        property_get_trash_contents_path,
        property_get_trash_contents_params,
        
        # trash\restore resource
        property_restore_resource_path,
        property_restore_resource_params,
        
        # async operation/operations
        property_async_operation_options,
        
        # async operation/get operation id
        property_operation_id,
        property_get_operation_status_params,
    ]
    credentials: List[flow.NodeType.Credential] = [
        flow.NodeType.Credential(
            name='yandex_api_oauth2', required=True),
    ]

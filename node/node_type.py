from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import CredentialProtocol, Defaults, DisplayOptions
from uc_flow_schemas.flow import NodeType as BaseNodeType
from uc_flow_schemas.flow import OptionValue, Property, RunState

from node.enums import DelFileOrFolderParams, MediaTypes, \
    FilesAndFoldersOperations, Params, \
    PreviewSizes, Resources, UserDiskOptions
from node.properties.params_for_flat_list import \
    property_with_params_for_get_flat_list


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
        Property(
            displayName='Operations',
            name='user_disk_operations',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Get meta information',
                    value=UserDiskOptions.get_meta_info,
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resources.user_disk,
                    ],
                },
            ),
        ),
        Property(
            displayName='Params',
            name='user_disk_params',
            type=Property.Type.COLLECTION,
            options=[
                Property(
                    displayName='Fields',
                    name=Params.fields,
                    type=Property.Type.STRING,
                    default='',
                    values=[
                        Property(
                            displayName='Fields',
                            name=Params.fields,
                            type=Property.Type.STRING,
                            default='',
                            placeholder='Список полей в ответе',
                        ),
                    ],
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resources.user_disk,
                    ],
                    'user_disk_operations': [
                        UserDiskOptions.get_meta_info,
                    ],
                },
            ),
        ),
        
        # files and folders\operations
        Property(
            displayName='Operation',
            name='files_and_folders_operations',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Delete file or folder',
                    value=FilesAndFoldersOperations.del_file_or_folder,
                ),
                OptionValue(
                    name='Upload file',
                    value=FilesAndFoldersOperations.upload_file,
                ),
                OptionValue(
                    name='Get flat list',
                    value=FilesAndFoldersOperations.get_flat_list,
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resources.files_and_folders,
                    ],
                },
            ),
        ),
        
        # files and folders\delete file or folder
        Property(
            displayName='Path',
            name='path_to_delete',
            type=Property.Type.STRING,
            required=True,
            description='Путь к файлу или каталогу',
            default='',
            placeholder='folder/file.txt',
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resources.files_and_folders,
                    ],
                    'files_and_folders_operations': [
                        FilesAndFoldersOperations.del_file_or_folder,
                    ],
                },
            ),
        ),
        Property(
            displayName='Params',
            name='delete_params',
            type=Property.Type.COLLECTION,
            options=[
                Property(
                    displayName='Permanently',
                    name=DelFileOrFolderParams.permanently,
                    type=Property.Type.BOOLEAN,
                    default=False,
                    values=[
                        Property(
                            displayName='Permanently',
                            name=DelFileOrFolderParams.permanently,
                            type=Property.Type.BOOLEAN,
                            default=False,
                            placeholder='признак безвозвратного удаления',
                        ),
                    ],
                ),
                Property(
                    displayName='Fields',
                    name=DelFileOrFolderParams.fields,
                    type=Property.Type.STRING,
                    default='',
                    values=[
                        Property(
                            displayName='Fields',
                            name=DelFileOrFolderParams.fields,
                            type=Property.Type.STRING,
                            default='',
                            placeholder='Список полей в ответе',
                        ),
                    ],
                ),
                Property(
                    displayName='Force async',
                    name=DelFileOrFolderParams.force_async,
                    type=Property.Type.BOOLEAN,
                    default=False,
                    values=[
                        Property(
                            displayName='Force async',
                            name=DelFileOrFolderParams.force_async,
                            type=Property.Type.BOOLEAN,
                            default=False,
                            placeholder='Выполнить асинхронно.',
                        ),
                    ],
                ),
                Property(
                    displayName='md5',
                    name=DelFileOrFolderParams.md5,
                    type=Property.Type.STRING,
                    default='',
                    values=[
                        Property(
                            displayName='md5',
                            name=DelFileOrFolderParams.md5,
                            type=Property.Type.STRING,
                            default='',
                            placeholder='md5 удаляемого файла.',
                        ),
                    ],
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resources.files_and_folders,
                    ],
                    'files_and_folders_operations': [
                        FilesAndFoldersOperations.del_file_or_folder,
                    ],
                },
            ),
        ),
        
        # files and folders\upload file
        Property(
            displayName='Download link',
            name='download_link',
            type=Property.Type.STRING,
            required=True,
            default='',
            description='Ссылка для скачивания файла',
            displayOptions=DisplayOptions(
                show={
                    'files_and_folders_operations': [
                        FilesAndFoldersOperations.upload_file,
                    ],
                    'resource': [
                        Resources.files_and_folders,
                    ],
                },
            ),
        ),
        Property(
            displayName='File_name',
            name='file_name',
            type=Property.Type.STRING,
            required=True,
            default='',
            description='Имя файла',
            displayOptions=DisplayOptions(
                show={
                    'files_and_folders_operations': [
                        FilesAndFoldersOperations.upload_file,
                    ],
                    'resource': [
                        Resources.files_and_folders,
                    ],
                },
            ),
        ),
        
        # files and folders\get flat list
        property_with_params_for_get_flat_list,
        
    ]

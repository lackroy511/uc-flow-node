from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import CredentialProtocol, Defaults, DisplayOptions
from uc_flow_schemas.flow import NodeType as BaseNodeType
from uc_flow_schemas.flow import OptionValue, Property, RunState

from node.enums import DelFileOrFolderParams, GetMetaInfoParams, MediaTypes, \
    FilesAndFoldersOperations, Params, \
    PreviewSizes, Resources, UpdateMetaInfoParams, UserDiskOptions
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
                    name='Get meta info',
                    value=FilesAndFoldersOperations.get_meta_info,
                ),
                OptionValue(
                    name='Update meta info',
                    value=FilesAndFoldersOperations.update_meta_info,
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
        
        # files and folders\get meta info
        Property(
            displayName='Path',
            name='get_meta_info_path',
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
                        FilesAndFoldersOperations.get_meta_info,
                    ],
                },
            ),
        ),
        Property(
            displayName='Params',
            name='get_meta_info_params',
            type=Property.Type.COLLECTION,
            options=[
                Property(
                    displayName='Fields',
                    name=GetMetaInfoParams.fields,
                    type=Property.Type.STRING,
                    default='',
                    values=[
                        Property(
                            displayName='Fields',
                            name=GetMetaInfoParams.fields,
                            type=Property.Type.STRING,
                            default='',
                            placeholder='Список полей в ответе',
                        ),
                    ],
                ),
                Property(
                    displayName='Limit',
                    name=GetMetaInfoParams.limit,
                    type=Property.Type.NUMBER,
                    default=20,
                    values=[
                        Property(
                            displayName='Limit',
                            name=GetMetaInfoParams.limit,
                            type=Property.Type.NUMBER,
                            default='',
                            placeholder='Количество ресурсов в ответе',
                        ),
                    ],
                ),
                Property(
                    displayName='Offset',
                    name=GetMetaInfoParams.offset,
                    type=Property.Type.NUMBER,
                    default='',
                    values=[
                        Property(
                            displayName='Offset',
                            name=GetMetaInfoParams.offset,
                            type=Property.Type.NUMBER,
                            default='',
                            placeholder='Количество ресурсов с начала списка',
                        ),
                    ],
                ),
                Property(
                    displayName='Preview size',
                    name=GetMetaInfoParams.preview_size,
                    type=Property.Type.OPTIONS,
                    default='',
                    values=[
                        Property(
                            displayName='Preview size',
                            name=GetMetaInfoParams.preview_size,
                            type=Property.Type.OPTIONS,
                            default='',
                            placeholder='Размер уменьшенного изображения',
                            options=[
                                OptionValue(
                                    name=PreviewSizes.S_SIZE,
                                    value=PreviewSizes.S_SIZE,
                                ),
                                OptionValue(
                                    name=PreviewSizes.M_SIZE,
                                    value=PreviewSizes.M_SIZE,
                                ),
                                OptionValue(
                                    name=PreviewSizes.L_SIZE,
                                    value=PreviewSizes.L_SIZE,
                                ),
                                OptionValue(
                                    name=PreviewSizes.XL_SIZE,
                                    value=PreviewSizes.XL_SIZE,
                                ),
                                OptionValue(
                                    name=PreviewSizes.XXL_SIZE,
                                    value=PreviewSizes.XXL_SIZE,
                                ),
                                OptionValue(
                                    name=PreviewSizes.XXXL_SIZE,
                                    value=PreviewSizes.XXXL_SIZE,
                                ),
                            ],
                        ),
                    ],
                ),
                Property(
                    displayName='Preview crop',
                    name=GetMetaInfoParams.preview_crop,
                    type=Property.Type.BOOLEAN,
                    default='',
                    values=[
                        Property(
                            displayName='Preview crop',
                            name=GetMetaInfoParams.preview_crop,
                            type=Property.Type.BOOLEAN,
                            default='',
                            placeholder='Обрезать превью согласно размеру',
                        ),
                    ],
                ),
                Property(
                    displayName='Sort by',
                    name=GetMetaInfoParams.sort,
                    type=Property.Type.STRING,
                    default='',
                    values=[
                        Property(
                            displayName='Sort by',
                            name=GetMetaInfoParams.sort,
                            type=Property.Type.STRING,
                            default='',
                            placeholder='name,path,created,modified,size ',
                        ),
                    ],
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'files_and_folders_operations': [
                        FilesAndFoldersOperations.get_meta_info,
                    ],
                    'resource': [
                        Resources.files_and_folders,
                    ],
                },
            ),
        ),
        
        # files and folders\update meta info
        Property(
            displayName='Path',
            name='update_meta_info_path',
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
                        FilesAndFoldersOperations.update_meta_info,
                    ],
                },
            ),
        ),
        Property(
            displayName='Body',
            name='body',
            type=Property.Type.JSON,
            required=True,
            description='Добавляемые атрибуты к свойствам объекта JSON.',
            default={
                'custom_properties': {'fields': 'values'},
            },
            placeholder='Новые свойства в JSON формате',
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resources.files_and_folders,
                    ],
                    'files_and_folders_operations': [
                        FilesAndFoldersOperations.update_meta_info,
                    ],
                },
            ),
        ),
        Property(
            displayName='Params',
            name='update_meta_info_params',
            type=Property.Type.COLLECTION,
            options=[
                Property(
                    displayName='Fields',
                    name=UpdateMetaInfoParams.fields,
                    type=Property.Type.STRING,
                    default='',
                    values=[
                        Property(
                            displayName='Fields',
                            name=UpdateMetaInfoParams.fields,
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
                        Resources.files_and_folders,
                    ],
                    'files_and_folders_operations': [
                        FilesAndFoldersOperations.update_meta_info,
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

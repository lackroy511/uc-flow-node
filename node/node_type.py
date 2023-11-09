from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import CredentialProtocol, Defaults, DisplayOptions
from uc_flow_schemas.flow import NodeType as BaseNodeType
from uc_flow_schemas.flow import OptionValue, Property, RunState

from node.enums import MediaTypes, Operations, Params, PreviewSizes, Resources


class NodeType(flow.NodeType):
    id: str = 'd0654eef-83eb-484f-9275-bdd0f8ca7ae4'
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
        
        # files and folders\operation
        Property(
            displayName='Operation',
            name='operation',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Upload file',
                    value=Operations.upload_file,
                ),
                OptionValue(
                    name='Get flat list',
                    value=Operations.get_flat_list,
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
                    'operation': [
                        Operations.upload_file,
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
                    'operation': [
                        Operations.upload_file,
                    ],
                    'resource': [
                        Resources.files_and_folders,
                    ],
                },
            ),
        ),
        
        # files and folders\get flat list
        Property(
            displayName='Params',
            name='params',
            type=Property.Type.COLLECTION,
            options=[
                Property(
                    displayName='Limit',
                    name=Params.limit,
                    type=Property.Type.NUMBER,
                    default=20,
                    values=[
                        Property(
                            displayName='Limit',
                            name='limit',
                            type=Property.Type.NUMBER,
                            default='',
                            placeholder='Количество файлов в запросе',
                        ),
                    ],
                ),
                Property(
                    displayName='Media type',
                    name=Params.media_type,
                    type=Property.Type.MULTI_OPTIONS,
                    default='',
                    values=[
                        Property(
                            displayName='Media type',
                            name='media_type',
                            type=Property.Type.MULTI_OPTIONS,
                            default='',
                            placeholder='Тип возвращаемых файлов',
                            options=[
                                OptionValue(
                                    name=MediaTypes.audio,
                                    value=MediaTypes.audio,
                                ),
                                OptionValue(
                                    name=MediaTypes.backup,
                                    value=MediaTypes.backup,
                                ),
                                OptionValue(
                                    name=MediaTypes.book,
                                    value=MediaTypes.book,
                                ),
                                OptionValue(
                                    name=MediaTypes.compressed,
                                    value=MediaTypes.compressed,
                                ),
                                OptionValue(
                                    name=MediaTypes.data,
                                    value=MediaTypes.data,
                                ),
                                OptionValue(
                                    name=MediaTypes.development,
                                    value=MediaTypes.development,
                                ),
                                OptionValue(
                                    name=MediaTypes.diskimage,
                                    value=MediaTypes.diskimage,
                                ),
                                OptionValue(
                                    name=MediaTypes.document,
                                    value=MediaTypes.document,
                                ),
                                OptionValue(
                                    name=MediaTypes.encoded,
                                    value=MediaTypes.encoded,
                                ),
                                OptionValue(
                                    name=MediaTypes.executable,
                                    value=MediaTypes.executable,
                                ),
                                OptionValue(
                                    name=MediaTypes.flash,
                                    value=MediaTypes.flash,
                                ),
                                OptionValue(
                                    name=MediaTypes.font,
                                    value=MediaTypes.font,
                                ),
                                OptionValue(
                                    name=MediaTypes.image,
                                    value=MediaTypes.image,
                                ),
                                OptionValue(
                                    name=MediaTypes.settings,
                                    value=MediaTypes.settings,
                                ),
                                OptionValue(
                                    name=MediaTypes.spreadsheet,
                                    value=MediaTypes.spreadsheet,
                                ),
                                OptionValue(
                                    name=MediaTypes.text,
                                    value=MediaTypes.text,
                                ),
                                OptionValue(
                                    name=MediaTypes.unknown,
                                    value=MediaTypes.unknown,
                                ),
                                OptionValue(
                                    name=MediaTypes.video,
                                    value=MediaTypes.video,
                                ),
                                OptionValue(
                                    name=MediaTypes.web,
                                    value=MediaTypes.web,
                                ),  
                            ],
                        ),
                    ],
                ),
                Property(
                    displayName='Offset',
                    name=Params.offset,
                    type=Property.Type.NUMBER,
                    default='',
                    values=[
                        Property(
                            displayName='Offset',
                            name=Params.offset,
                            type=Property.Type.NUMBER,
                            default='',
                            placeholder='Количество ресурсов с начала списка',
                        ),
                    ],
                ),
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
                            placeholder='Список свойств JSON в ответе',
                        ),
                    ],
                ),
                Property(
                    displayName='Preview size',
                    name=Params.preview_size,
                    type=Property.Type.OPTIONS,
                    default='',
                    values=[
                        Property(
                            displayName='Preview size',
                            name=Params.preview_size,
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
                    name=Params.preview_crop,
                    type=Property.Type.BOOLEAN,
                    default='',
                    values=[
                        Property(
                            displayName='Preview crop',
                            name=Params.preview_crop,
                            type=Property.Type.BOOLEAN,
                            default='',
                            placeholder='Обрезать превью согласно размеру',
                        ),
                    ],
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'operation': [
                        Operations.get_flat_list,
                    ],
                    'resource': [
                        Resources.files_and_folders,
                    ],
                },
            ),
        ),
    ]

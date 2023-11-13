from uc_flow_schemas.flow import DisplayOptions, OptionValue, Property

from node.enums import (CopyFileOrFolderParams, CreateFolderParams,
                        DelFileOrFolderParams, FilesAndFoldersOperations,
                        GetFileInBase64Params, GetMetaInfoParams, MediaTypes,
                        Params, PreviewSizes, PublicFilesAndFoldersOperations,
                        PublicFilesAndFoldersParams, Resources, 
                        TrashOperations, TrashParams,
                        UpdateMetaInfoParams, UserDiskOptions)

property_user_disk_params = Property(
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
)

property_delete_params = Property(
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
)

property_get_meta_info_params = Property(
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
)

property_update_meta_info_params = Property(
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
)

property_create_folder_params = Property(
    displayName='Params',
    name='create_folder_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=CreateFolderParams.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=CreateFolderParams.fields,
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
                FilesAndFoldersOperations.create_folder,
            ],
        },
    ),
)

property_get_flat_list_params = Property(
    displayName='Params',
    name='get_flat_list_params',
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
                    placeholder='Список полей в ответе',
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
            'files_and_folders_operations': [
                FilesAndFoldersOperations.get_flat_list,
            ],
            'resource': [
                Resources.files_and_folders,
            ],
        },
    ),
)

property_copy_file_or_folder_params = Property(
    displayName='Params',
    name='copy_file_or_folder_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=CopyFileOrFolderParams.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=CopyFileOrFolderParams.fields,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Список полей в ответе',
                ),
            ],
        ),
        Property(
            displayName='Force Async',
            name=CopyFileOrFolderParams.force_async,
            type=Property.Type.BOOLEAN,
            default=False,
            values=[
                Property(
                    displayName='Force Async',
                    name=CopyFileOrFolderParams.force_async,
                    type=Property.Type.BOOLEAN,
                    default=False,
                    placeholder='Список возвращаемых атрибутов.',
                ),
            ],
        ),
        Property(
            displayName='Overwrite',
            name=CopyFileOrFolderParams.overwrite,
            type=Property.Type.BOOLEAN,
            default=False,
            values=[
                Property(
                    displayName='Overwrite',
                    name=CopyFileOrFolderParams.overwrite,
                    type=Property.Type.BOOLEAN,
                    default=False,
                    placeholder='Список возвращаемых атрибутов.',
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
                FilesAndFoldersOperations.copy_file_or_folder,
            ],
        },
    ),
)

property_get_file_in_base64_params = Property(
    displayName='Params',
    name='get_file_in_base64_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=GetFileInBase64Params.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=GetFileInBase64Params.fields,
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
                FilesAndFoldersOperations.get_file_in_base64,
            ],
        },
    ),
)

property_get_flat_list_ordered_by_date_params = Property(
    displayName='Params',
    name='get_flat_list_ordered_by_date_params',
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
            'files_and_folders_operations': [
                FilesAndFoldersOperations.get_flat_list_ordered_by_date,
            ],
            'resource': [
                Resources.files_and_folders,
            ],
        },
    ),
)

property_move_file_or_folder_params = Property(
    displayName='Params',
    name='move_file_or_folder_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=CopyFileOrFolderParams.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=CopyFileOrFolderParams.fields,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Список полей в ответе',
                ),
            ],
        ),
        Property(
            displayName='Force Async',
            name=CopyFileOrFolderParams.force_async,
            type=Property.Type.BOOLEAN,
            default=False,
            values=[
                Property(
                    displayName='Force Async',
                    name=CopyFileOrFolderParams.force_async,
                    type=Property.Type.BOOLEAN,
                    default=False,
                    placeholder='Список возвращаемых атрибутов.',
                ),
            ],
        ),
        Property(
            displayName='Overwrite',
            name=CopyFileOrFolderParams.overwrite,
            type=Property.Type.BOOLEAN,
            default=False,
            values=[
                Property(
                    displayName='Overwrite',
                    name=CopyFileOrFolderParams.overwrite,
                    type=Property.Type.BOOLEAN,
                    default=False,
                    placeholder='Список возвращаемых атрибутов.',
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
                FilesAndFoldersOperations.move_file_or_folder,
            ],
        },
    ),
)

property_get_public_resource_list_params = Property(
    displayName='Params',
    name='get_public_resource_list_params',
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
                    placeholder='Смещение от начала списка ресурсов.',
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
        Property(
            displayName='Type',
            name='type',
            type=Property.Type.OPTIONS,
            default='',
            values=[
                Property(
                    displayName='Type',
                    name='type',
                    type=Property.Type.OPTIONS,
                    default='',
                    placeholder='Фильтр по типам ресурсов.',
                    options=[
                        OptionValue(
                            name='file',
                            value='file',
                        ),
                        OptionValue(
                            name='dir',
                            value='dir',
                        ),  
                    ],
                ),
            ],
        ),
    ],
    displayOptions=DisplayOptions(
        show={
            'files_and_folders_operations': [
                FilesAndFoldersOperations.get_public_resource_list,
            ],
            'resource': [
                Resources.files_and_folders,
            ],
        },
    ),
)
####
property_publish_resource_params = Property(
    displayName='Params',
    name='publish_resource_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=GetFileInBase64Params.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=GetFileInBase64Params.fields,
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
                FilesAndFoldersOperations.publish_resource,
            ],
        },
    ),
)

property_unpublish_resource_params = Property(
    displayName='Params',
    name='unpublish_resource_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=GetFileInBase64Params.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=GetFileInBase64Params.fields,
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
                FilesAndFoldersOperations.unpublish_resource,
            ],
        },
    ),
)

property_get_upload_link_params = Property(
    displayName='Params',
    name='get_upload_link_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=GetFileInBase64Params.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=GetFileInBase64Params.fields,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Список полей в ответе',
                ),
            ],
        ),
        Property(
            displayName='Overwrite',
            name=CopyFileOrFolderParams.overwrite,
            type=Property.Type.BOOLEAN,
            default=False,
            values=[
                Property(
                    displayName='Overwrite',
                    name=CopyFileOrFolderParams.overwrite,
                    type=Property.Type.BOOLEAN,
                    default=False,
                    placeholder='Перезаписать существующий файл.',
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
                FilesAndFoldersOperations.get_upload_link,
            ],
        },
    ),
)

property_get_public_meta_info_params = Property(
    displayName='Params',
    name='get_public_meta_info_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=PublicFilesAndFoldersParams.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=GetFileInBase64Params.fields,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Список полей в ответе',
                ),
            ],
        ),
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
            displayName='Path',
            name=PublicFilesAndFoldersParams.path,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Path',
                    name=PublicFilesAndFoldersParams.path,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Путь к ресурсу в публичной папке.',
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
            'resource': [
                Resources.public_files_and_folders,
            ],
            'public_files_and_folders_operations': [
                PublicFilesAndFoldersOperations.get_meta_info,
            ],
        },
    ),
)

property_get_download_link_params = Property(
    displayName='Params',
    name='get_download_link_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=PublicFilesAndFoldersParams.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=GetFileInBase64Params.fields,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Список полей в ответе',
                ),
            ],
        ),
        Property(
            displayName='Path',
            name=PublicFilesAndFoldersParams.path,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Path',
                    name=PublicFilesAndFoldersParams.path,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Путь к ресурсу в публичной папке.',
                ),
            ],
        ),
    ],
    displayOptions=DisplayOptions(
        show={
            'resource': [
                Resources.public_files_and_folders,
            ],
            'public_files_and_folders_operations': [
                PublicFilesAndFoldersOperations.get_download_link,
            ],
        },
    ),
)

property_save_resource_params = Property(
    displayName='Params',
    name='save_resource_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=PublicFilesAndFoldersParams.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=GetFileInBase64Params.fields,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Путь к копируемому ресурсу' + 
                                ' в публичной папке.',
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
            displayName='Name',
            name=PublicFilesAndFoldersParams.name,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Name',
                    name=PublicFilesAndFoldersParams.name,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Имя сохраняемого ресурса.',
                ),
            ],
        ),
        Property(
            displayName='Path',
            name=PublicFilesAndFoldersParams.path,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Path',
                    name=PublicFilesAndFoldersParams.path,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Путь к копируемому ресурсу' + 
                                ' в публичной папке.',
                ),
            ],
        ),
        Property(
            displayName='Save path',
            name=PublicFilesAndFoldersParams.save_path,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Save path',
                    name=PublicFilesAndFoldersParams.save_path,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Путь к папке, в которую будет' + 
                                ' сохранен ресурс. По умолчанию «Загрузки».',
                ),
            ],
        ),
    ],
    displayOptions=DisplayOptions(
        show={
            'resource': [
                Resources.public_files_and_folders,
            ],
            'public_files_and_folders_operations': [
                PublicFilesAndFoldersOperations.save_resource,
            ],
        },
    ),
)

property_empty_trash_params = Property(
    displayName='Params',
    name='empty_trash_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=TrashParams.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=TrashParams.fields,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Список полей в ответе',
                ),
            ],
        ),
        Property(
            displayName='Force async',
            name=TrashParams.force_async,
            type=Property.Type.BOOLEAN,
            default=False,
            values=[
                Property(
                    displayName='Force async',
                    name=TrashParams.force_async,
                    type=Property.Type.BOOLEAN,
                    default=False,
                    placeholder='Выполнить асинхронно.',
                ),
            ],
        ),
        Property(
            displayName='Path',
            name=TrashParams.path,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Path',
                    name=TrashParams.path,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Путь к ресурсу в Корзине.',
                ),
            ],
        ),
    ],
    displayOptions=DisplayOptions(
        show={
            'resource': [
                Resources.trash,
            ],
            'trash_operations': [
                TrashOperations.empty_trash,
            ],
        },
    ),
)

property_get_trash_contents_params = Property(
    displayName='Params',
    name='get_trash_contents_params',
    type=Property.Type.COLLECTION,
    options=[
        Property(
            displayName='Fields',
            name=TrashParams.fields,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Fields',
                    name=TrashParams.fields,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='Список полей в ответе',
                ),
            ],
        ),
        Property(
            displayName='Limit',
            name=TrashParams.limit,
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
            displayName='Offset',
            name=TrashParams.offset,
            type=Property.Type.NUMBER,
            default='',
            values=[
                Property(
                    displayName='Offset',
                    name=TrashParams.offset,
                    type=Property.Type.NUMBER,
                    default='',
                    placeholder='Количество ресурсов с начала списка',
                ),
            ],
        ),
        Property(
            displayName='Preview size',
            name=TrashParams.preview_size,
            type=Property.Type.OPTIONS,
            default='',
            values=[
                Property(
                    displayName='Preview size',
                    name=TrashParams.preview_size,
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
            name=TrashParams.preview_crop,
            type=Property.Type.BOOLEAN,
            default=False,
            values=[
                Property(
                    displayName='Preview crop',
                    name=TrashParams.preview_crop,
                    type=Property.Type.BOOLEAN,
                    default=False,
                    placeholder='Обрезать превью согласно размеру',
                ),
            ],
        ),
        Property(
            displayName='Sort by',
            name=TrashParams.sort,
            type=Property.Type.STRING,
            default='',
            values=[
                Property(
                    displayName='Sort by',
                    name=TrashParams.sort,
                    type=Property.Type.STRING,
                    default='',
                    placeholder='name,path,created,modified,size ',
                ),
            ],
        ),
    ],
    displayOptions=DisplayOptions(
        show={
            'trash_operations': [
                TrashOperations.get_trash_contents,
            ],
            'resource': [
                Resources.trash,
            ],
        },
    ),
)

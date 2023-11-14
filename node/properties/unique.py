from uc_flow_schemas.flow import DisplayOptions, Property

from node.enums import AsyncOpOperations, FilesAndFoldersOperations, Resources

property_body = Property(
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
)

property_download_link = Property(
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
)

property_file_name = Property(
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
)

property_operation_id = Property(
    displayName='Operation id',
    name='operation_id',
    type=Property.Type.STRING,
    required=True,
    default='',
    description='Идентификатор операции.',
    displayOptions=DisplayOptions(
        show={
            'async_operation_operations': [
                AsyncOpOperations.get_operation_status,
            ],
            'resource': [
                Resources.async_operation,
            ],
        },
    ),
)

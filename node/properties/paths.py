from uc_flow_schemas.flow import DisplayOptions, OptionValue, Property

from node.enums import FilesAndFoldersOperations, Resources, TrashOperations

property_path_to_delete = Property(
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
)

property_get_meta_info_path = Property(
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
)

property_update_meta_info_path = Property(
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
)

property_create_folder_path = Property(
    displayName='Path',
    name='create_folder_path',
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
                FilesAndFoldersOperations.create_folder,
            ],
        },
    ),
)

property_copy_from_path = Property(
    displayName='From',
    name='copy_from_path',
    type=Property.Type.STRING,
    required=True,
    description='Путь к копируемому ресурсу.',
    default='',
    placeholder='folder/file.txt',
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

property_copy_to_path = Property(
    displayName='Path',
    name='copy_to_path',
    type=Property.Type.STRING,
    required=True,
    description='Путь к создаваемому ресурсу.',
    default='',
    placeholder='folder/file.txt',
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

property_get_file_in_base64_path = Property(
    displayName='Path',
    name='get_file_in_base64_path',
    type=Property.Type.STRING,
    required=True,
    description='Путь к ресурсу.',
    default='',
    placeholder='folder/file.txt',
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

property_move_from_path = Property(
    displayName='From',
    name='move_from_path',
    type=Property.Type.STRING,
    required=True,
    description='Путь к перемещаемому ресурсу.',
    default='',
    placeholder='folder/file.txt',
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

property_move_to_path = Property(
    displayName='Path',
    name='move_to_path',
    type=Property.Type.STRING,
    required=True,
    description='Путь к создаваемому ресурсу.',
    default='',
    placeholder='folder/file.txt',
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

property_publish_resource_path = Property(
    displayName='Path',
    name='publish_resource_path',
    type=Property.Type.STRING,
    required=True,
    description='Путь к публикуемому ресурсу.',
    default='',
    placeholder='folder/file.txt',
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

property_unpublish_resource_path = Property(
    displayName='Path',
    name='unpublish_resource_path',
    type=Property.Type.STRING,
    required=True,
    description='Путь к ресурсу.',
    default='',
    placeholder='folder/file.txt',
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

property_get_upload_link_path = Property(
    displayName='Path',
    name='get_upload_link_path',
    type=Property.Type.STRING,
    required=True,
    description='Путь к загружаемому файлу на Диске.',
    default='',
    placeholder='folder/file.txt',
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

property_get_trash_contents_path = Property(
    displayName='Path',
    name='get_trash_contents_path',
    type=Property.Type.STRING,
    required=True,
    description='Путь к ресурсу в Корзине.',
    default='',
    placeholder='folder/file.txt',
    displayOptions=DisplayOptions(
        show={
            'resource': [
                Resources.trash,
            ],
            'trash_operations': [
                TrashOperations.get_trash_contents,
            ],
        },
    ),
)

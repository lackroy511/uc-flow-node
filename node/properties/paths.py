from uc_flow_schemas.flow import DisplayOptions, OptionValue, Property

from node.enums import FilesAndFoldersOperations, Resources

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

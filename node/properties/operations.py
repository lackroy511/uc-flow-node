from uc_flow_schemas.flow import DisplayOptions, OptionValue, Property

from node.enums import FilesAndFoldersOperations, Resources, UserDiskOptions

property_user_disk_operations = Property(
    displayName='Operation',
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
)

property_files_and_folders_operations = Property(
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
            name='Create folder',
            value=FilesAndFoldersOperations.create_folder,
        ),
        OptionValue(
            name='Copy file or folder',
            value=FilesAndFoldersOperations.copy_file_or_folder,
        ),
        OptionValue(
            name='Get file in base64',
            value=FilesAndFoldersOperations.get_file_in_base64,
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
)

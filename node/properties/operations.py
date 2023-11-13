from uc_flow_schemas.flow import DisplayOptions, OptionValue, Property

from node.enums import (FilesAndFoldersOperations,
                        PublicFilesAndFoldersOperations, Resources,
                        UserDiskOptions)

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
        OptionValue(
            name='Get flat list ordered by download date',
            value=FilesAndFoldersOperations.get_flat_list_ordered_by_date,
        ),
        OptionValue(
            name='Move file or folder',
            value=FilesAndFoldersOperations.move_file_or_folder,
        ),
        OptionValue(
            name='Get public resource list',
            value=FilesAndFoldersOperations.get_public_resource_list,
        ),
        OptionValue(
            name='Publish resource',
            value=FilesAndFoldersOperations.publish_resource,
        ),
        OptionValue(
            name='Unpublish resource',
            value=FilesAndFoldersOperations.unpublish_resource,
        ),
        OptionValue(
            name='Get upload link',
            value=FilesAndFoldersOperations.get_upload_link,
        ),
        OptionValue(
            name='Upload file',
            value=FilesAndFoldersOperations.upload_file,
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

property_public_files_and_folders_operations = Property(
    displayName='Operation',
    name='public_files_and_folders_operations',
    type=Property.Type.OPTIONS,
    noDataExpression=True,
    options=[
        OptionValue(
            name='Get meta info',
            value=PublicFilesAndFoldersOperations.get_meta_info,
        ),
        OptionValue(
            name='Get download link',
            value=PublicFilesAndFoldersOperations.get_download_link,
        ),
        OptionValue(
            name='Save resource to download folder',
            value=PublicFilesAndFoldersOperations.save_resource,
        ),
    ],
    displayOptions=DisplayOptions(
        show={
            'resource': [
                Resources.public_files_and_folders,
            ],
        },
    ),
)

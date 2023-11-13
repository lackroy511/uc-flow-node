from uc_flow_schemas.flow import DisplayOptions, OptionValue, Property

from node.enums import PublicFilesAndFoldersOperations, Resources

property_get_meta_info_public_key = Property(
    displayName='Public_key',
    name='get_meta_info_public_key',
    type=Property.Type.STRING,
    required=True,
    description='Ключ или публичный URL ресурса.',
    default='',
    placeholder='',
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

from enum import Enum


class Resources(str, Enum):
    user_disk = 'User disk'
    files_and_folders = 'Files and folders'


class UserDiskOptions(str, Enum):
    get_meta_info = 'get_meta_info'


class FilesAndFoldersOperations(str, Enum):
    del_file_or_folder = 'del_file_or_folder'
    upload_file = 'upload_file'
    get_meta_info = 'get_meta_info'
    update_meta_info = 'update_meta_info'
    create_folder = 'create_folder'
    copy_file_or_folder = 'copy_file_or_folder'
    get_file_in_base64 = 'get_file_in_base64'
    
    get_flat_list = 'get_flat_list'
    

class MediaTypes(str, Enum):
    audio = 'audio'
    backup = 'backup'
    book = 'book'
    compressed = 'compressed'
    data = 'data'
    development = 'development'
    diskimage = 'diskimage'
    document = 'document'
    encoded = 'encoded'
    executable = 'executable'
    flash = 'flash'
    font = 'font'
    image = 'image'
    settings = 'settings'
    spreadsheet = 'spreadsheet'
    text = 'text'
    unknown = 'unknown'
    video = 'video'
    web = 'web'


class DelFileOrFolderParams(str, Enum):
    path = 'path'
    permanently = 'permanently'
    fields = 'fields'
    force_async = 'force_async'
    md5 = 'md5'


class GetMetaInfoParams(str, Enum):
    path = 'path'
    fields = 'fields'
    limit = 'limit'
    offset = 'offset'
    preview_crop = 'preview_crop'
    preview_size = 'preview_size'
    sort = 'sort'


class UpdateMetaInfoParams(str, Enum):
    fields = 'fields' 


class CreateFolderParams(str, Enum):
    fields = 'fields' 


class CopyFileOrFolderParams(str, Enum):
    fields = 'fields'
    force_async = 'force_async'
    overwrite = 'overwrite'


class GetFileInBase64Params(str, Enum):
    fields = 'fields'


class Params(str, Enum):
    limit = 'limit'
    media_type = 'media_type'
    offset = 'offset'
    fields = 'fields'
    preview_size = 'preview_size'
    preview_crop = 'preview_crop'
    

class PreviewSizes(str, Enum):
    S_SIZE = 'S'
    M_SIZE = 'M'
    L_SIZE = 'L'
    XL_SIZE = 'XL'
    XXL_SIZE = 'XXL'
    XXXL_SIZE = 'XXXL'

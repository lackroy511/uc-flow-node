from enum import Enum


class Operations(str, Enum):
    upload_file = 'upload_file'
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


class Params:
    limit = 'limit'
    media_type = 'media_type'
    offset = 'offset'
    fields = 'fields'
    preview_size = 'preview_size'
    preview_crop = 'preview_crop'
    

class PreviewSizes:
    S_SIZE = 'S'
    M_SIZE = 'M'
    L_SIZE = 'L'
    XL_SIZE = 'XL'
    XXL_SIZE = 'XXL'
    XXXL_SIZE = 'XXXL'

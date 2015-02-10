from ctypes import *


_libexif = CDLL('libexif.so')

EXIF_IFD_COUNT = 5


class _ExifEntry(Structure):
    _fields_ = [
        ('tag', c_uint),
        ('format', c_uint),
        ('components', c_uint),
        ('data', c_void_p),
        ('size', c_uint),
        ('parent', c_void_p),
        ('priv', c_void_p),
    ]


class _ExifData(Structure):
    _fields_ = [
        ('ifd', c_void_p * EXIF_IFD_COUNT),
        ('data', c_void_p),
        ('size', c_uint),
        ('priv', c_void_p),
    ]


class ExifTags(object):
    EXIF_TAG_INTEROPERABILITY_INDEX = 0x0001
    EXIF_TAG_INTEROPERABILITY_VERSION = 0x0002
    EXIF_TAG_NEW_SUBFILE_TYPE = 0x00fe
    EXIF_TAG_IMAGE_WIDTH = 0x0100
    EXIF_TAG_IMAGE_LENGTH = 0x0101
    EXIF_TAG_BITS_PER_SAMPLE = 0x0102
    EXIF_TAG_COMPRESSION = 0x0103
    EXIF_TAG_PHOTOMETRIC_INTERPRETATION = 0x0106
    EXIF_TAG_FILL_ORDER = 0x010a
    EXIF_TAG_DOCUMENT_NAME = 0x010d
    EXIF_TAG_IMAGE_DESCRIPTION = 0x010e
    EXIF_TAG_MAKE = 0x010f
    EXIF_TAG_MODEL = 0x0110
    EXIF_TAG_STRIP_OFFSETS = 0x0111
    EXIF_TAG_ORIENTATION = 0x0112
    EXIF_TAG_SAMPLES_PER_PIXEL = 0x0115
    EXIF_TAG_ROWS_PER_STRIP = 0x0116
    EXIF_TAG_STRIP_BYTE_COUNTS = 0x0117
    EXIF_TAG_X_RESOLUTION = 0x011a
    EXIF_TAG_Y_RESOLUTION = 0x011b
    EXIF_TAG_PLANAR_CONFIGURATION = 0x011c
    EXIF_TAG_RESOLUTION_UNIT = 0x0128
    EXIF_TAG_TRANSFER_FUNCTION = 0x012d
    EXIF_TAG_SOFTWARE = 0x0131
    EXIF_TAG_DATE_TIME = 0x0132
    EXIF_TAG_ARTIST = 0x013b
    EXIF_TAG_WHITE_POINT = 0x013e
    EXIF_TAG_PRIMARY_CHROMATICITIES = 0x013f
    EXIF_TAG_SUB_IFDS = 0x014a
    EXIF_TAG_TRANSFER_RANGE = 0x0156
    EXIF_TAG_JPEG_PROC = 0x0200
    EXIF_TAG_JPEG_INTERCHANGE_FORMAT = 0x0201
    EXIF_TAG_JPEG_INTERCHANGE_FORMAT_LENGTH = 0x0202
    EXIF_TAG_YCBCR_COEFFICIENTS = 0x0211
    EXIF_TAG_YCBCR_SUB_SAMPLING = 0x0212
    EXIF_TAG_YCBCR_POSITIONING = 0x0213
    EXIF_TAG_REFERENCE_BLACK_WHITE = 0x0214
    EXIF_TAG_XML_PACKET = 0x02bc
    EXIF_TAG_RELATED_IMAGE_FILE_FORMAT = 0x1000
    EXIF_TAG_RELATED_IMAGE_WIDTH = 0x1001
    EXIF_TAG_RELATED_IMAGE_LENGTH = 0x1002
    EXIF_TAG_CFA_REPEAT_PATTERN_DIM = 0x828d
    EXIF_TAG_CFA_PATTERN = 0x828e
    EXIF_TAG_BATTERY_LEVEL = 0x828f
    EXIF_TAG_COPYRIGHT = 0x8298
    EXIF_TAG_EXPOSURE_TIME = 0x829a
    EXIF_TAG_FNUMBER = 0x829d
    EXIF_TAG_IPTC_NAA = 0x83bb
    EXIF_TAG_IMAGE_RESOURCES = 0x8649
    EXIF_TAG_EXIF_IFD_POINTER = 0x8769
    EXIF_TAG_INTER_COLOR_PROFILE = 0x8773
    EXIF_TAG_EXPOSURE_PROGRAM = 0x8822
    EXIF_TAG_SPECTRAL_SENSITIVITY = 0x8824
    EXIF_TAG_GPS_INFO_IFD_POINTER = 0x8825
    EXIF_TAG_ISO_SPEED_RATINGS = 0x8827
    EXIF_TAG_OECF = 0x8828
    EXIF_TAG_TIME_ZONE_OFFSET = 0x882a
    EXIF_TAG_EXIF_VERSION = 0x9000
    EXIF_TAG_DATE_TIME_ORIGINAL = 0x9003
    EXIF_TAG_DATE_TIME_DIGITIZED = 0x9004
    EXIF_TAG_COMPONENTS_CONFIGURATION = 0x9101
    EXIF_TAG_COMPRESSED_BITS_PER_PIXEL = 0x9102
    EXIF_TAG_SHUTTER_SPEED_VALUE = 0x9201
    EXIF_TAG_APERTURE_VALUE = 0x9202
    EXIF_TAG_BRIGHTNESS_VALUE = 0x9203
    EXIF_TAG_EXPOSURE_BIAS_VALUE = 0x9204
    EXIF_TAG_MAX_APERTURE_VALUE = 0x9205
    EXIF_TAG_SUBJECT_DISTANCE = 0x9206
    EXIF_TAG_METERING_MODE = 0x9207
    EXIF_TAG_LIGHT_SOURCE = 0x9208
    EXIF_TAG_FLASH = 0x9209
    EXIF_TAG_FOCAL_LENGTH = 0x920a
    EXIF_TAG_SUBJECT_AREA = 0x9214
    EXIF_TAG_TIFF_EP_STANDARD_ID = 0x9216
    EXIF_TAG_MAKER_NOTE = 0x927c
    EXIF_TAG_USER_COMMENT = 0x9286
    EXIF_TAG_SUB_SEC_TIME = 0x9290
    EXIF_TAG_SUB_SEC_TIME_ORIGINAL = 0x9291
    EXIF_TAG_SUB_SEC_TIME_DIGITIZED = 0x9292
    EXIF_TAG_XP_TITLE = 0x9c9b
    EXIF_TAG_XP_COMMENT = 0x9c9c
    EXIF_TAG_XP_AUTHOR = 0x9c9d
    EXIF_TAG_XP_KEYWORDS = 0x9c9e
    EXIF_TAG_XP_SUBJECT = 0x9c9f
    EXIF_TAG_FLASH_PIX_VERSION = 0xa000
    EXIF_TAG_COLOR_SPACE = 0xa001
    EXIF_TAG_PIXEL_X_DIMENSION = 0xa002
    EXIF_TAG_PIXEL_Y_DIMENSION = 0xa003
    EXIF_TAG_RELATED_SOUND_FILE = 0xa004
    EXIF_TAG_INTEROPERABILITY_IFD_POINTER = 0xa005
    EXIF_TAG_FLASH_ENERGY = 0xa20b
    EXIF_TAG_SPATIAL_FREQUENCY_RESPONSE = 0xa20c
    EXIF_TAG_FOCAL_PLANE_X_RESOLUTION = 0xa20e
    EXIF_TAG_FOCAL_PLANE_Y_RESOLUTION = 0xa20f
    EXIF_TAG_FOCAL_PLANE_RESOLUTION_UNIT = 0xa210
    EXIF_TAG_SUBJECT_LOCATION = 0xa214
    EXIF_TAG_EXPOSURE_INDEX = 0xa215
    EXIF_TAG_SENSING_METHOD = 0xa217
    EXIF_TAG_FILE_SOURCE = 0xa300
    EXIF_TAG_SCENE_TYPE = 0xa301
    EXIF_TAG_NEW_CFA_PATTERN = 0xa302
    EXIF_TAG_CUSTOM_RENDERED = 0xa401
    EXIF_TAG_EXPOSURE_MODE = 0xa402
    EXIF_TAG_WHITE_BALANCE = 0xa403
    EXIF_TAG_DIGITAL_ZOOM_RATIO = 0xa404
    EXIF_TAG_FOCAL_LENGTH_IN_35MM_FILM = 0xa405
    EXIF_TAG_SCENE_CAPTURE_TYPE = 0xa406
    EXIF_TAG_GAIN_CONTROL = 0xa407
    EXIF_TAG_CONTRAST = 0xa408
    EXIF_TAG_SATURATION = 0xa409
    EXIF_TAG_SHARPNESS = 0xa40a
    EXIF_TAG_DEVICE_SETTING_DESCRIPTION = 0xa40b
    EXIF_TAG_SUBJECT_DISTANCE_RANGE = 0xa40c
    EXIF_TAG_IMAGE_UNIQUE_ID = 0xa420
    EXIF_TAG_GAMMA = 0xa500
    EXIF_TAG_PRINT_IMAGE_MATCHING = 0xc4a5
    EXIF_TAG_PADDING = 0xea1c


class ExifFormats(object):
    EXIF_FORMAT_BYTE = 1  # 1
    EXIF_FORMAT_ASCII = 2
    EXIF_FORMAT_SHORT = 3
    EXIF_FORMAT_LONG = 4
    EXIF_FORMAT_RATIONAL = 5
    EXIF_FORMAT_SBYTE = 6
    EXIF_FORMAT_UNDEFINED = 7
    EXIF_FORMAT_SSHORT = 8
    EXIF_FORMAT_SLONG = 9
    EXIF_FORMAT_SRATIONAL = 10
    EXIF_FORMAT_FLOAT = 11
    EXIF_FORMAT_DOUBLE = 12


# auto gen lookup tables
EXIF_TAG_NAMES = filter(lambda x: x.startswith('EXIF_'), dir(ExifTags))
EXIF_TAG_NAME_LOOKUP = dict((getattr(ExifTags, x), x) for x in EXIF_TAG_NAMES)
EXIF_FORMAT_NAMES = filter(lambda x: x.startswith('EXIF_'), dir(ExifFormats))
EXIF_FORMAT_NAME_LOOKUP = dict((getattr(ExifFormats, x), x) for x in EXIF_FORMAT_NAMES)

# defining functions result type
_exif_data_new_from_file = _libexif.exif_data_new_from_file
_exif_data_new_from_file.restype = POINTER(_ExifData)
_exif_data_new_from_data = _libexif.exif_data_new_from_data
_exif_data_new_from_data.restype = POINTER(_ExifData)
_exif_content_get_entry = _libexif.exif_content_get_entry
_exif_content_get_entry.restype = POINTER(_ExifEntry)


class ExifData(object):
    _data = None

    def __init__(self, data):
        self._data = data
        self._byte_order = _libexif.exif_data_get_byte_order(self._data)

    def get_byte_order(self):
        return self._byte_order

    def get_exif_entry(self, tag):
        """
        get a ExifEntry by tag.
        if found, a pointer of _ExifEntry will be returned
        if not found, None will be returned.
        """
        result = None
        for p in self._data[0].ifd:
            result = _exif_content_get_entry(p, c_uint(tag))
            if result:
                break

        return result

    def dump_exif_entry(self, tag):
        """
        find exif entry by tag, and dump as string
        """
        entry = self.get_exif_entry(tag)
        if not entry:
            return

        buf = (c_ubyte * 1024)()
        _libexif.exif_entry_get_value(entry, byref(buf), c_uint(sizeof(buf)))
        return '%s - %s' % (EXIF_TAG_NAME_LOOKUP.get(tag), bytearray(buf))

    def free(self):
        """
        Do not forget call free to release your exif data
        """
        if self._data:
            _libexif.exif_data_free(self._data)
            self._data = None
            self._byte_order = None


class Exif(object):

    @classmethod
    def exif_data_from_file(cls, filename):
        assert isinstance(filename, basestring)
        exifdata = _exif_data_new_from_file(c_char_p(filename))
        return ExifData(exifdata) if exifdata else None

    @classmethod
    def exif_data_from_data(cls, data):
        exifdata = _exif_data_new_from_data(data, c_uint(len(data)))
        return ExifData(exifdata) if exifdata else None


if __name__ == '__main__':
    # testing goes here
    import sys

    if len(sys.argv) != 2:
        print 'Usage:\n\t%s <filename>' % __file__
        sys.exit(-1)

    data = Exif.exif_data_from_file(sys.argv[1])
    print 'EXIF byte order = %s' % data.get_byte_order()

    for name in EXIF_TAG_NAMES:
        tag = getattr(ExifTags, name)
        dump = data.dump_exif_entry(tag)
        if dump:
            print dump
    data.free()

    print '--------------------------------------------------'

    data = Exif.exif_data_from_data(open(sys.argv[1]).read())
    for name in EXIF_TAG_NAMES:
        tag = getattr(ExifTags, name)
        dump = data.dump_exif_entry(tag)
        if dump:
            print dump
    data.free()

from ctypes import *
from pprint import pprint


class ExifLoader(object):
    _libexif = CDLL('libexif.so')
    _open_mode = None
    _exif = None

    def write_file(self, filename):
        assert isinstance(filename, basestring)
        self._libexif.exif_loader_write_file(self._exif, c_char_p(filename))

    def write(self, buf):
        self._libexif.exif_loader_write(self._exif, c_void_p(buf), c_uint(len(buf)))

    def __init__(self):
        self._exif = c_void_p(_libexif.exif_loader_new())


if __name__ == '__main__':
    # testing goes here
    exif = ExifLoader()
    exif.write_file('sample.jpg')
    pprint(dir(exif))

    import pdb; pdb.set_trace()
        

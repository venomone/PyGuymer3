def load_EXIF(fname, python = True):
    # Load sub-functions ...
    from .load_EXIF1 import load_EXIF1
    from .load_EXIF2 import load_EXIF2

    # Check what the user wants ...
    if python:
        # Will use the Python module "exifread" ...
        return load_EXIF1(fname)
    else:
        # Will use the binary "exiftool" ...
        return load_EXIF2(fname)

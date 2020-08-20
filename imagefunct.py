import exifread
from datetime import datetime

def get_date(filename):
    # read datetime from exif data of provided image
    f = open(filename, 'rb')
    tags = exifread.process_file(f)
    print(tags)
    # TODO: use file DateTime if datetime original is not present
    if not tags["EXIF DateTimeOriginal"]:
        dt = tags["DateTime"]
    dt = tags["EXIF DateTimeOriginal"]
    date_object = datetime.strptime(str(dt), "%Y:%m:%d %H:%M:%S")
    return date_object
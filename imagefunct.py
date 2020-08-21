import exifread
from datetime import datetime
import os
from PIL import Image

def get_date(filename):
    # read datetime from exif data of provided image
    f = open(filename, 'rb')
    tags = exifread.process_file(f)
    # Check if a date is provided inside EXIF information
    if "EXIF DateTimeOriginal" in tags:
        dt = tags["EXIF DateTimeOriginal"]
    elif "DateTime" in tags:
        dt = tags["DateTime"]
    else:
        dt = os.path.getctime(filename)
        return datetime.fromtimestamp(dt).strftime("%Y-%m-%d %H:%M:%S")
    return datetime.strptime(str(dt), "%Y:%m:%d %H:%M:%S")

def generate_thumbnail(filename):
    # generate a thumbnail image
    size = (200,200)
    im = Image.open(filename)
    im.thumbnail(size)
    thumbnail_filename = "thumbnail_"+ filename
    im.save("./static/thumbnails/" + thumbnail_filename)
    return thumbnail_filename
    # store in static/thumbnails
import exifread
from datetime import datetime
import os
from PIL import Image
from app import app
from os import walk

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
    size = (500,500)
    im = Image.open(app.config['UPLOAD_FOLDER'] + filename)
    im.thumbnail(size)
    thumbnail_filename = "thumbnail_"+ filename
    im.save("./static/thumbnails/" + thumbnail_filename)
    return thumbnail_filename
    # store in static/thumbnails

def scan_and_generate():
    filenames = []
    for dirpath, dirs, files in walk(app.config['UPLOAD_FOLDER']):
        filenames.extend(files)
        break
    filenames.remove("PUT_FILES_HERE")
    for file in filenames:
        generate_thumbnail(file)
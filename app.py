from flask import Flask, redirect, render_template, request
from os import walk

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

@app.route('/')
def hello():
    filenames = []
    for dirpath, dirs, files in walk(FILE_UPLOADS):
        filenames.extend(files)
        break
    filenames.remove("PUT_FILES_HERE")
    return render_template('index.html', filenames=filenames)

@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Submit file to database
        redirect('/')
    else:
        return render_template('upload.html')
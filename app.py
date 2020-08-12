from flask import Flask, redirect, render_template, request
from os import path, walk
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")


UPLOAD_FOLDER = 'static/uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif', '.mov']

@app.route('/')
def gallery():
    filenames = []
    for dirpath, dirs, files in walk(app.config['UPLOAD_FOLDER']):
        filenames.extend(files)
        break
    filenames.remove("PUT_FILES_HERE")
    return render_template('index.html', filenames=filenames)

@app.route('/upload', methods=["GET", "POST"])
def upload_files():
    if request.method == "POST":
        for uploaded_file in request.files.getlist('file'):
            if uploaded_file.filename != '':
                filename = secure_filename(uploaded_file.filename)
                uploaded_file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/')
    else:
        return render_template('upload.html')
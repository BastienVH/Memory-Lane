from flask import Flask, redirect, render_template, request
from os import path, walk, getenv, environ
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

# Setup View (only accessible on first launch)
@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if getenv('SETUP_MODE') != 'Setup_true':
        return redirect('/')
    else:
        if request.method == "POST":
            # make supplied email admin
            # change SETUP_MODE to False in .env
            fin = open(".flaskenv", "rt")
            data = fin.read()
            data = data.replace('Setup_true', 'Setup_false')
            fin.close
            fin = open(".flaskenv", "wt")
            fin.write(data)
            fin.close()
            # directly set env SETUP_MODE to false
            environ['SETUP_MODE'] = 'Setup_false'
            return 'posting setup'
        else:
            return render_template('setup.html')

# Main gallery view
@app.route('/')
def gallery():
    filenames = []
    for dirpath, dirs, files in walk(app.config['UPLOAD_FOLDER']):
        filenames.extend(files)
        break
    filenames.remove("PUT_FILES_HERE")
    return render_template('index.html', filenames=filenames)

# Batch upload view
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
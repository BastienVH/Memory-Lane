from flask import Flask, redirect, render_template, request
from os import path, walk, getenv, environ
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_sqlalchemy import SQLAlchemy
from config import Config, DevelopmentConfig, TestingConfig, ProductionConfig

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, Image
from imagefunct import get_date, generate_thumbnail, scan_and_generate

# Setup View (only accessible on first launch)
@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if getenv('SETUP_MODE') != 'Setup_true':
        return redirect('/')
    else:
        if request.method == "POST":
            # make supplied email admin
            admin = User(request.form['username'], request.form['email'], True)
            db.session.add(admin)
            db.session.commit()
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
    images = Image.query.order_by(Image.date_taken.desc()).all()
    print(images)
    return render_template('index.html', images=images)

# Batch upload view
@app.route('/upload', methods=["GET", "POST"])
def upload_files():
    if request.method == "POST":
        for uploaded_file in request.files.getlist('file'):
            if uploaded_file.filename != '':
                filename = secure_filename(uploaded_file.filename)
                hashed_filename = hash(filename)
                save_path = path.join(app.config['UPLOAD_FOLDER'], str(hashed_filename)+".jpg")
                uploaded_file.save(save_path)
                date_taken = get_date(save_path)
                thumbnail_filename = generate_thumbnail(str(hashed_filename) + ".jpg")
                newImage = Image(filename, hashed_filename, date_taken, thumbnail_filename)
                db.session.add(newImage)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('upload.html')

# Invite view
@app.route('/invite', methods=['GET', 'POST'])
def invite():
    if request.method == 'POST':
        # Add email addresses to db
        users = request.form['email'].splitlines()
        print(users)
        for user in users:
            newUser = User(None, user, False)
            db.session.add(newUser)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('invite.html')
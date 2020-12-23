from flask import Flask, redirect, render_template, request
from os import path, walk, getenv, environ
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_sqlalchemy import SQLAlchemy
from config import Config, DevelopmentConfig, TestingConfig, ProductionConfig
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECURITY_PASSWORD_SALT'] = getenv('SECURITY_PASSWORD_SALT')
app.config['SECURITY_PASSWORDLESS'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = getenv('MAIL_PASSWORD')
mail = Mail(app)
db = SQLAlchemy(app)

from models import Users, Roles, Images
from imagefunct import get_date, generate_thumbnail, scan_and_generate

user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)
security = Security(app, user_datastore)

# Setup View (only accessible on first launch)
@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if getenv('SETUP_MODE') != 'Setup_true':
        return redirect('/')
    else:
        if request.method == "POST":
            # make supplied email admin
            # admin = Users(request.form['username'], request.form['email'], True)
            user_datastore.create_user(username=request.form['username'] ,email=request.form['email'], password=request.form['password'])
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
@login_required
def gallery():
    images = Images.query.order_by(Images.date_taken.desc()).all()
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
                newImage = Images(filename, hashed_filename, date_taken, thumbnail_filename)
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
        useremails = request.form['email'].splitlines()
        for useremail in useremails:
            user_datastore.create_user(
                email = useremail
            )
            # newUser = User(None, user, False)
            # db.session.add(newUser)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('invite.html')
from app import db

# db configuration
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, is_admin):
        self.username = username
        self.email = email
        self.is_admin = is_admin
    
    def __repr__(self):
        return '<User %r>' % self.username

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orig_filename = db.Column(db.String(255))
    hashed_filename = db.Column(db.String(255), unique=True)
    date_taken = db.Column(db.DateTime)

    def __init__(self, orig_filename, hashed_filename, date_taken):
        self.orig_filename = orig_filename
        self.hashed_filename = hashed_filename
        self.date_taken = date_taken
    
    def __repr__(self):
        return '<image %r>' % self.orig_filename
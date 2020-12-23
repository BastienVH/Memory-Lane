from app import db
from flask_security import UserMixin, RoleMixin

# db configuration
roles_users_table = db.Table('roles_users',
    db.Column('users_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('roles_id', db.Integer(), db.ForeignKey('roles.id'))
)

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(80))
    active = db.Column(db.Boolean())
    roles = db.relationship(
        'Roles',
        secondary=roles_users_table,
        backref='user', lazy=True)
    # is_admin = db.Column(db.Boolean, default=False)

    # def __init__(self, username, email, is_admin):
    #     self.username = username
    #     self.email = email
    #     self.is_admin = is_admin
    
    # def __repr__(self):
    #     return '<User %r>' % self.username

class Roles(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orig_filename = db.Column(db.String(255))
    hashed_filename = db.Column(db.String(255), unique=True)
    date_taken = db.Column(db.DateTime)
    thumbnail_filename = db.Column(db.String(255), unique=True)

    def __init__(self, orig_filename, hashed_filename, date_taken, thumbnail_filename):
        self.orig_filename = orig_filename
        self.hashed_filename = hashed_filename
        self.date_taken = date_taken
        self.thumbnail_filename = thumbnail_filename
    
    def __repr__(self):
        return '<image %r>' % self.orig_filename
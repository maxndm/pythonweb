# This means import object "db" from "." - "." means current package which is "website"
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(200))
    surname = db.Column(db.String(200))
    photoname = db.Column(db.String(100))

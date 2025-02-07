from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128),nullable=False)
    user_group_id = db.Column(db.Integer, db.ForeignKey('user_group.id'))

class UserGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(128), nullable=False)

    user = db.relationship("User", backref="usergroup", lazy=True)
    

class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)

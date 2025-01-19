from flask import Flask, jsonify,request 
from flask_migrate import Migrate
from models import User, UserGroup ,db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

Migrate = Migrate(app, db)

db.init_app(app)

from views import *

app.register_blueprint(user_bp)
app.register_blueprint(user_group_bp)
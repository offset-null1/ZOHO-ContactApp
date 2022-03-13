from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MongoEngine(app)
api = Api(app)
bcrypt = Bcrypt(app)

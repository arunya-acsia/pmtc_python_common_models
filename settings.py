import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask


app = Flask(__name__, template_folder="templates")


if app.config['ENV'] == 'dev':
	app.config.from_object("config.DevelopmentConfig")


if app.config['ENV'] == 'test':
	app.config.from_object("config.TestingConfig")


db = SQLAlchemy(app)
migrate = Migrate(app, db)
marshmallow = Marshmallow(app)

basedir = os.path.abspath(os.path.dirname(__file__))

import os
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig

basedir = os.path.abspath(os.path.dirname(__file__))

if os.path.exists("logs/backend.log"):
    os.remove("logs/backend.log")
with open(basedir + "/logging_config.yml") as logger_config:
    log_config_dict = yaml.safe_load(logger_config.read())
dictConfig(log_config_dict)

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'data.sqlite') + '?check_same_thread=False'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flask_app)
from app import main_routes
from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from xml.dom.minidom import parse
import xml.dom.minidom
import datetime
import time

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# enable CORS
CORS(app)

# 注册 blueprint
from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')





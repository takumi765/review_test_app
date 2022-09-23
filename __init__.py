from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.config')
db = SQLAlchemy(app)

from models import test  # 追加

import views

""" import views """
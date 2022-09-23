from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # 追加

app = Flask(__name__)
app.config.from_object('testapp.config')

db = SQLAlchemy(app)  # 追加

from .models import employee  # 追加

import testapp.views
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.BaseConfiguration')
db = SQLAlchemy(app)

from ctfscore import views, models

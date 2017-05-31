from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

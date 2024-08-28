from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'SECRET_KEY'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from . import models, views  # noqa

db.create_all()

# cd C:\Users\Proffesional\PycharmProjects\pythonProject2\4\4.7\flask_shortener
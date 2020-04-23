"""TODO"""
from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import DATE, Column

from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class UserGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    level = db.Column(db.Integer)
    dificulty = db.Column(db.String(6))
    current_game = db.Column(db.String(90))
    solution = db.Column(db.String(90))

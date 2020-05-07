"""DataBase models"""
from flask_login import UserMixin  # pylint: disable=import-error
from flask_sqlalchemy.model import DefaultMeta
from . import db

BaseModel: DefaultMeta = db.Model


class User(UserMixin, BaseModel):
    """User model"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class UserGame(BaseModel):
    """User current game"""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    level = db.Column(db.Integer)
    dificulty = db.Column(db.String(6))
    current_game = db.Column(db.String(90))
    sudoku_game = db.Column(db.String(90))

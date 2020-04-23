"""TODO"""
import requests
from flask import Blueprint, render_template
from flask_login import current_user, login_required

from project.models import UserGame

from . import db

routes = Blueprint("main", __name__, template_folder="../templates")


@routes.route("/")
def index():
    return render_template("index.html")


@routes.route("/games")
@login_required
def games():
    return render_template("games.html", name=current_user.name)


@routes.route("/sudoku/<string:dificulty>")
@login_required
def play_game(dificulty):
    load_game = UserGame.query.filter_by(
        user_id=current_user.id, dificulty=dificulty
    ).first()
    if not load_game:
        new_game = requests.get(f"0.0.0.0:8000/sudoku/game/{dificulty}/0")
        # TODO
    return render_template(
        "sudoku.html",
        sudoku=load_game.current_game,
        level=load_game.level,
        dificulty=dificulty,
        solution=load_game.solution,
    )

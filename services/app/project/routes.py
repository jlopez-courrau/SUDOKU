"""TODO"""
import requests
from flask import Blueprint, render_template, jsonify
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
def sudoku(dificulty):
    load_game = UserGame.query.filter_by(
        user_id=current_user.id, dificulty=dificulty
    ).first()
    if not load_game or load_game.current_game == load_game.solution:
        level = load_game.level + 1 if load_game else 0
        sudoku_request = requests.get(
            f"http://data-provider:8000/sudoku/game/{dificulty}/{level}"
        )
        if sudoku_request.status_code == 200:
            data = sudoku_request.json()
            load_game = UserGame(
                user_id=current_user.id,
                current_game=data["sudoku"],
                level=data["level"],
                dificulty=data["dificulty"],
                solution=data["solution"],
            )
            db.session.add(load_game)
            db.session.commit()
        else:
            render_template("Error.html", message=sudoku_request)

    return render_template(
        "sudoku.html",
        sudoku=load_game.current_game,
        level=load_game.level,
        dificulty=dificulty,
        solution=load_game.solution,
    )


@routes.route("/sudoku/add/move/<string:dificulty>/<int:index>", methods=["PUT"])
@login_required
def sudoku_add_move(dificulty, index):
    result = False
    game_over = False
    load_game = UserGame.query.filter_by(
        user_id=current_user.id, dificulty=dificulty
    ).first()
    if not load_game or load_game.current_game != load_game.solution:
        current_game = list(load_game.current_game)
        current_game[index] = load_game.solution[index]
        load_game.current_game = "".join(current_game)
        db.session.commit()
        result = True
        game_over = load_game.current_game == load_game.solution
    return jsonify(result=result, game_over=game_over)

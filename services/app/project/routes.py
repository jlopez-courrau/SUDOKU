"""Application main functionality"""
from flask import Blueprint, render_template, jsonify
from flask_login import current_user, login_required  # pylint: disable=import-error
from project.provider_requests import (
    request_sudoku_game,
    request_sudoku_valid,
    request_sudoku_complete,
)
from project.validations import is_sudoku_option
from project.models import UserGame
from . import db

routes = Blueprint("main", __name__, template_folder="../templates")


@routes.route("/")
def index():
    """application first page"""
    return render_template("index.html")


@routes.route("/games")
@login_required
def games():
    """load the select game dificulty page"""
    return render_template("games.html", name=current_user.name)


@routes.route("/sudoku/<string:dificulty>")
@login_required
def sudoku(dificulty: str):
    """loads SUDOKU board game"""
    load_game = UserGame.query.filter_by(
        user_id=current_user.id, dificulty=dificulty
    ).first()

    is_game_over = (
        request_sudoku_complete(load_game.current_game) if load_game else False
    )

    if not load_game or is_game_over:
        level = load_game.level + 1 if load_game else 0
        load_game = request_sudoku_game(dificulty, level)
        if load_game.sudoku_game:
            load_game.user_id = current_user.id
            db.session.add(load_game)
            db.session.commit()
    return render_template(
        "sudoku.html",
        sudoku=load_game.sudoku_game,
        user_game=load_game.current_game,
        level=load_game.level,
        dificulty=dificulty,
    )


@routes.route("/sudoku/move/valid/<string:move>")
def sudoku_valid_move(move: str):
    """validate valid move (1~9)"""
    return jsonify(result=is_sudoku_option(move), move=move)


@routes.route(
    "/sudoku/move/<string:dificulty>/<int:position>/<int:move>", methods=["PUT"]
)
@login_required
def sudoku_move(dificulty: str, position: int, move: int):
    """TODO"""
    valid = False
    game_over = False
    load_game = UserGame.query.filter_by(
        user_id=current_user.id, dificulty=dificulty
    ).first()
    if load_game:
        list_game = list(load_game.current_game)
        list_game[position] = str(move)
        current_game = "".join(list_game)
        valid_move = request_sudoku_valid(current_game)
        if valid_move:
            valid = True
            load_game.current_game = current_game
            game_over = request_sudoku_complete(load_game.current_game)
            db.session.add(load_game)
            db.session.commit()

    return jsonify(valid=valid, game_over=game_over)

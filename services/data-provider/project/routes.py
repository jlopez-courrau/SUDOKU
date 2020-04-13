"""
Application routes
"""
from flask import jsonify, request
from project import app
from project.sudoku import get_sudoku_game, valid_game, is_game_compelte


@app.route("/")
def index():
    '''Simple Hello response'''
    return jsonify(message="Hello from data-provider")


@app.route("/sudoku/game")
def get_game():
    '''get sudoku game'''
    param_level = request.args.get("level", default="easy")
    param_index = int(request.args.get("index", default=0))
    sudoku_game, sudoku_solution, sudoku_level, sudoku_index = \
        get_sudoku_game(param_level, param_index)

    return jsonify(
        level=sudoku_level,
        index=sudoku_index,
        sudoku=sudoku_game,
        solution=sudoku_solution
    )


@app.route("/sudoku/valid")
def get_valid_game():
    '''check if a sudoku is valid'''
    sudoku = request.args.get("sudoku")

    if not sudoku:
        return jsonify("Invalid request"), 406

    result = valid_game(sudoku)
    return jsonify(result=result, sudoku=sudoku)


@app.route("/sudoku/complete")
def get_is_game_complete():
    '''check if a sudoku is complete and valid '''
    sudoku = request.args.get("sudoku")

    if not sudoku:
        return jsonify("Invalid request"), 406

    result = is_game_compelte(sudoku)
    return jsonify(result=result, sudoku=sudoku)


# add others routes here

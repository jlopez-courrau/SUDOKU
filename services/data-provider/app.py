"""SUDOKU provider"""
# pylint: disable=unused-import

from flask.cli import FlaskGroup
from project import app
from project.routes import index, get_game, get_valid_game, get_is_game_complete


cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()

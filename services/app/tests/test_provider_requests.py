"""Data-provider Unit test"""
# pylint: disable=C0116, C0301, W0621

from project.provider_requests import (
    request_sudoku_game,
    request_sudoku_valid,
    request_sudoku_complete,
    port,
    provider,
    base_url,
)


def test_request_sudoku_easy():
    user_game = request_sudoku_game("easy", 0)

    assert user_game.dificulty == "easy"
    assert user_game.level == 0
    assert user_game.current_game == user_game.sudoku_game
    assert user_game.user_id == 0
    assert (
        user_game.sudoku_game
        == "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
    )


def test_request_sudoku_medium():
    user_game = request_sudoku_game("medium", 1)

    assert user_game.dificulty == "medium"
    assert user_game.level == 1
    assert user_game.current_game == user_game.sudoku_game
    assert user_game.user_id == 0
    assert (
        user_game.sudoku_game
        == "52...6.........7.13...........4..8..6......5...........418.........3..2...87....."
    )


def test_request_sodoku_no_game():
    user_game = request_sudoku_game("", 0)
    assert user_game.current_game is None
    assert user_game.id is None
    assert user_game.sudoku_game is None
    assert user_game.dificulty is None


def test_request_sudoku_valid():
    valid_sudoku = "245981376169273584837564219976125438513498627482736951391657842728349165654812793"

    assert request_sudoku_valid(valid_sudoku)


def test_request_sudoku_invalid():
    invalid_sudoku = "22..8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3"

    assert not request_sudoku_valid(invalid_sudoku)


def test_request_sudoku_complete():
    complete_sudoku = "245981376169273584837564219976125438513498627482736951391657842728349165654812793"

    assert request_sudoku_complete(complete_sudoku)


def test_request_sudoku_incomplete():
    incomplete_sudoku = "2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3"

    assert not request_sudoku_complete(incomplete_sudoku)


def test_request_params():
    assert port in base_url
    assert provider in base_url

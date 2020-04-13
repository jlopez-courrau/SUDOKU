"""
Unit test powered by pytest!!!
In this file can be found unit test for Sodoku routes
docstring have been set off from pylint as functions name are self explanatory
"""
# pylint: disable=C0116, W0621

import pytest
from project.routes import app


@pytest.fixture(scope="module")
def client():
    with app.test_client() as c:
        yield c


def test_hello_page(client):
    url = "/"

    response = client.get(url)

    assert response.status_code == 200
    assert b"Hello" in response.data


def test_sudoku_default(client):
    url = "/sudoku/game/"
    response = client.get(url)
    assert response.status_code == 200
    assert b"0" in response.data
    assert b"easy" in response.data
    assert b"level" in response.data
    assert b"dificulty" in response.data
    assert b"solution" in response.data
    assert b"sudoku" in response.data


def test_sudoku(client):
    url = "/sudoku/game/"
    param = "medium/1"

    response = client.get(url + param)

    assert response.status_code == 200
    assert b"0" not in response.data
    assert b"medium" in response.data
    assert b"dificulty" in response.data
    assert b"level" in response.data
    assert b"solution" in response.data
    assert b"sudoku" in response.data


def test_invalid_game(client):
    url = "/sudoku/valid/"
    param = (
        "..3.2.6..9.33.5..1..18.64....81.29..7.......8..67.82...."
        + "26.95..8..2.3..9..5.1.3.."
    )

    response = client.get(url + param)

    assert response.status_code == 200
    assert b"false" in response.data
    assert b"result" in response.data
    assert b"sudoku" in response.data


def test_valid_game(client):
    url = "/sudoku/valid/"
    param = (
        "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82...."
        + "26.95..8..2.3..9..5.1.3.."
    )

    response = client.get(url + param)

    assert response.status_code == 200
    assert b"true" in response.data
    assert b"result" in response.data
    assert b"sudoku" in response.data


def test_incomplete_game(client):
    url = "/sudoku/complete/"
    param = (
        "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82...."
        + "26.95..8..2.3..9..5.1.3.."
    )

    response = client.get(url + param)

    assert response.status_code == 200
    assert b"false" in response.data
    assert b"result" in response.data
    assert b"sudoku" in response.data


def test_complete_invalid_game(client):
    url = "/sudoku/complete/"
    param = (
        "333322669998336564134187643456817291172233445866677828891239"
        + "261952281123344955389"
    )

    response = client.get(url + param)

    assert response.status_code == 200
    assert b"false" in response.data
    assert b"result" in response.data
    assert b"sudoku" in response.data


def test_complete_game(client):
    url = "/sudoku/complete/"
    param = (
        "483921657967345821251876493548132976729564138136798245372689"
        + "514814253769695417382"
    )

    response = client.get(url + param)

    assert response.status_code == 200
    assert b"true" in response.data
    assert b"result" in response.data
    assert b"sudoku" in response.data

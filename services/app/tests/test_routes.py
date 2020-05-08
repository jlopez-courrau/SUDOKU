"""Routes Unit test!!!

In this file can be found unit test for Sodoku routes
auth not include in this file
docstring have been set off from pylint as functions name are self explanatory
"""
# pylint: disable=C0116, W0621

import pytest
from project import create_app


@pytest.fixture(scope="module")
def client():
    app = create_app()

    with app.test_client() as c:
        c.post("/signup", data={"email": "joe@joes.com", "password": "12345"})
        c.post("/login", data={"email": "joe@joes.com", "password": "12345"})
        yield c


def test_index(client):
    url = "/"
    response = client.get(url)
    assert response.status_code == 200


def test_games(client):
    url = "/games"
    response = client.get(url)
    assert response.status_code == 200
    assert b"/sudoku/easy" in response.data
    assert b"/sudoku/medium" in response.data
    assert b"/sudoku/hard" in response.data


def test_sudoku_easy(client):
    url = "/sudoku/"
    param = "easy"

    response = client.get(f"{url}{param}")
    assert response.status_code == 200


def test_sudoku_medium(client):
    url = "/sudoku/"
    param = "medium"

    response = client.get(f"{url}{param}")
    assert response.status_code == 200


def test_sudoku_hard(client):
    url = "/sudoku/"
    param = "hard"

    response = client.get(f"{url}{param}")
    assert response.status_code == 200


def test_valid_move(client):
    url = "/sudoku/move/valid/"
    for number in range(1, 10):
        response = client.get(f"{url}{str(number)}")
        assert response.status_code == 200
        assert b"true" in response.data
        assert b"result" in response.data


def test_invalid_move(client):
    url = "/sudoku/move/valid/"
    invalid_options = [" ", "-1", "0", "10", "a", "A", "-"]
    for value in invalid_options:
        response = client.get(f"{url}{value}")
        assert response.status_code == 200
        assert b"false" in response.data
        assert b"result" in response.data


def test_move(client):
    url = "/sudoku/move/"
    params = "easy/0/4"

    client.get("/sudoku/easy")
    response = client.put(f"{url}{params}")
    assert response.status_code == 200
    assert b"valid" in response.data
    assert b"game_over" in response.data


def test_move_not_allow(client):
    url = "/sudoku/move/"
    params = "easy/0/9"

    client.get("/sudoku/easy")
    response = client.put(f"{url}{params}")
    assert response.status_code == 200
    assert b"valid" in response.data
    assert b"game_over" in response.data


# LAST TEST!
def test_sudoku_no_login(client):
    url = "/sudoku/"
    param = "easy"

    client.get("/logout")
    response = client.get(f"{url}{param}")
    assert not response.status_code == 200

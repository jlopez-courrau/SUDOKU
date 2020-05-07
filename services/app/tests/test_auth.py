"""AUTH Unit test

In this file can be found unit test for authorization process
docstring have been set off from pylint as functions name are self explanatory
"""
# pylint: disable=C0116, W0621

import pytest
from project import create_app

credentials = {"email": "joe@joes.com", "password": "12345"}


@pytest.fixture(scope="module")
def client():
    with create_app().test_client() as c:
        yield c


def test_signup(client):
    url = "/signup"

    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, data=credentials)
    # 302 as redirect
    assert response.status_code == 302


def test_login(client):
    url = "/login"

    client.post("/signup", data=credentials)

    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, data=credentials)

    # 302 as redirect
    assert response.status_code == 302


def test_logout(client):
    url = "/logout"

    client.post("/signup", data=credentials)
    client.post("/login", data=credentials)
    response = client.get(url)

    # 302 as redirect
    assert response.status_code == 302

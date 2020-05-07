"""Data-Provider request in just one place"""
import requests
from project.models import UserGame

port = "8000"
provider = "data-provider"
base_url = f"http://{provider}:{port}/sudoku"


def request_sudoku_game(dificulty: str, level: int) -> UserGame:
    """game request"""
    game = UserGame()
    provider_request = requests.get(f"{base_url}/game/{dificulty}/{level}")
    if provider_request.status_code == 200:
        request_data = provider_request.json()
        game.current_game = request_data["sudoku"]
        game.sudoku_game = request_data["sudoku"]
        game.level = request_data["level"]
        game.dificulty = request_data["dificulty"]
        game.user_id = 0
    # TODO: add else raise exception
    return game


def request_sudoku_valid(sudoku: str) -> bool:
    """valid request"""
    is_valid = False
    provider_request = requests.get(f"{base_url}/valid/{sudoku}")
    if provider_request.status_code == 200:
        request_data = provider_request.json()
        is_valid = request_data["result"]
    # TODO: else raise exception
    return is_valid


def request_sudoku_complete(sudoku: str) -> bool:
    """complete game request"""
    is_complete = False
    provider_request = requests.get(f"{base_url}/complete/{sudoku}")
    if provider_request.status_code == 200:
        request_data = provider_request.json()
        is_complete = request_data["result"]
    # TODO: else raise exception
    return is_complete

"""
SUDOKU handler
for library documentation please go to: https://pypi.org/project/basicsudoku/
"""
from typing import Tuple
from basicsudoku import SudokuBoard, puzzles, solvers


def get_sudoku_game(
        level: str = "easy",
        index: int = 0
) -> Tuple[str, str, str, int]:
    """This method will return a SUDOKU and his solution

    :param level: complexity of the game
    :param index: game list index

    :return: game, game solution, level, index

    :raise:
        ValueError: Invalid difficulty level
        ValueError: Invalid index
        Exception: End of games
    """
    game = SudokuBoard()
    game.symbols, game_level, game_index = _get_puzzle(level, index)

    solution = SudokuBoard(game.symbols)
    solvers.BasicSolver(solution)
    return game.symbols, solution.symbols, game_level, game_index


def _get_puzzle(level: str, index: int) -> Tuple[str, str, int]:
    """This method get the sudoku game from library

    :param level: complexity of the game
    :param index: game list index
    :return:  sudoku symbols, level, index

    :raise:
        ValueError: Invalid difficulty level
        ValueError: Invalid index
        Exception: End of games
    """
    if index < 0:
        raise ValueError("Invalid index, should be a positive value")
    if level == "easy" or level.lower == "easy":
        if index < len(puzzles.easy50):
            return puzzles.easy50[index], level, index
        return _get_puzzle("medium", 0)
    if level == "medium" or level.lower == "medium":
        if index < len(puzzles.top95):
            return puzzles.top95[index], level, index
        return _get_puzzle("hard", 0)
    if level == "hard" or level.lower == "hard":
        if index < len(puzzles.hardest):
            return puzzles.hardest[index], level, index
        raise Exception("End of game", "no more games")
    raise ValueError("Invalid difficulty level")


def valid_game(sudoku: str) -> bool:
    """This method check if a sudoku is valid
    :param sudoku:  sudoku game
    @return:  valid game
    """
    if not "." in sudoku and "0" in sudoku:
        sudoku = sudoku.replace("0", ".")
    return SudokuBoard(symbols=sudoku, strict=False).is_valid_board()


def is_game_compelte(sudoku: str) -> bool:
    """This method check if a sudoku is complete
    :param sudoku:  sudoku game
    @return:  valid game
    """
    if not "." in sudoku and "0" in sudoku:
        sudoku = sudoku.replace("0", ".")
    board = SudokuBoard(symbols=sudoku, strict=False)
    return board.is_valid_board() and board.is_solved()

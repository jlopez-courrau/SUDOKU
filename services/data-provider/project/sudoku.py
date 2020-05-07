"""SUDOKU handler

for library documentation please go to: https://pypi.org/project/basicsudoku/
"""

from dataclasses import dataclass

from basicsudoku import SudokuBoard, puzzles, solvers


@dataclass
class SudokuGame:
    """Class for sudoku elements"""

    difficulty: str
    level: int
    sudoku: str
    solution: str

    def __init__(self, sudoku: str, difficulty: str, level: int):
        self.sudoku = sudoku
        self.difficulty = difficulty
        self.level = level
        self.solution = self._solve()

    def _solve(self) -> str:
        """This method will return the sudoku solution"""
        new_bord = SudokuBoard(self.sudoku)
        solvers.BasicSolver(new_bord)
        return new_bord.symbols


def get_sudoku_game(difficulty: str = "easy", level: int = 0) -> SudokuGame:
    """This method get the sudoku game from library

    :param difficulty: complexity of the game
    :param level: game list index
    :return:  sudoku, solution, index, difficulty wrap on SudokuGame dataclass

    :raise:
        ValueError: Invalid difficulty
        ValueError: Invalid level
        Exception: End of games
    """
    puzzle = None
    if level < 0:
        raise ValueError("Invalid level, should be a positive value")
    if difficulty == "easy" or difficulty.lower == "easy":
        if level >= len(puzzles.easy50):
            return get_sudoku_game("medium", 0)
        puzzle = puzzles.easy50[level]
    elif difficulty == "medium" or difficulty.lower == "medium":
        if level >= len(puzzles.top95):
            return get_sudoku_game("hard", 0)
        puzzle = puzzles.top95[level]
    elif difficulty == "hard" or difficulty.lower == "hard":
        if level >= len(puzzles.hardest):
            raise Exception("End of game", "no more games")
        puzzle = puzzles.hardest[level]
    if not puzzle:
        raise ValueError("Invalid difficulty")
    return SudokuGame(sudoku=puzzle, level=level, difficulty=difficulty)


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

"""Unit test for validations util"""
# pylint: disable=C0116
from project.validations import is_sudoku_option


def test_sudoku_valid_values():
    for number in range(1, 10):
        assert is_sudoku_option(str(number))


def test_sudoku_invalid_numbers():
    right_answer = False
    assert right_answer == is_sudoku_option("-1")
    assert right_answer == is_sudoku_option("0")
    assert right_answer == is_sudoku_option("10")


def test_sudoku_invalid_chars():
    right_answer = False
    assert right_answer == is_sudoku_option("a")
    assert right_answer == is_sudoku_option("A")
    assert right_answer == is_sudoku_option("-")
    assert right_answer == is_sudoku_option("")
    assert right_answer == is_sudoku_option(" ")

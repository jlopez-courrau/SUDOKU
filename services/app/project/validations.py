"""SUDOKU field validations"""
import re


def is_sudoku_option(value: str) -> bool:
    """validate the number is a integer between 1-9"""
    return bool(re.match(r"^[1-9]$", value))

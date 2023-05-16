"""
Exception classes for games
"""

class SudokuException(Exception):
    """
    Exception class for all Sudoku errors
    """
    def __init__(self, message: str) -> None:
        """
        create sudoku exception with error message
        """
        super().__init__(message)


class WordleException(Exception):
    """
    Exception class for all Wordle errors
    """
    def __init__(self, message: str) -> None:
        """
        create sudoku exception with error message
        """
        super().__init__(message)
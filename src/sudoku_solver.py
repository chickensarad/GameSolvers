from typing import Literal
from exceptions import SudokuException

class Sudoku:
    """
    Sudoku board of 9x9, all rows, all columns, and all 3x3 boxes must contain one and only one of numbers 1 through 9
    """
    def __init__(self, board: list[list[str]]):
        if len(board) != 9:
            raise SudokuException(
                f'Unexpected number of rows: the number of rows should be 9. The number rows is {len(board)}'
            )
        for row in range(9):
            if len(board[row]) != 9:
                raise SudokuException(
                    f'Unexpected number of columns: the number of columns should be 9. The number of columns in row{row} is {len(board[row])}'
                )
            for square in board[row]:
                if (not isinstance(square, str)) or (square not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.']):
                    raise SudokuException(
                        f'Unexpected character: all squares on sudoku board must be of type str and a number between 1-9 or a . in case of unknown.'
                    )
        self.board = board


    def displayBoard(self) -> None:
        """
        display the sudoku board
        """
        for row in range(len(self.board)):
            if row % 3 == 0 and row != 0:
                print("- - - - - - - - - - - - - - - -")
            for col in range(len(self.board[0])):
                if col % 3 == 0 and col != 0:
                    print("|  ", end="")
                if col == 8:
                    print(self.board[row][col])
                else:
                    print(self.board[row][col] + "  ", end="")
    def getLineBox(self, board: list[list[str]], row: int, col: int, mode: Literal['row', 'col', 'box']) -> list:
        """
        get flattened list of line or box
        """
        possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        if mode == 'row':
            return [int(board[row][i]) for i in range(9) if board[row][i] != '.']
        if mode == 'col':
            return [int(board[i][col]) for i in range(9) if board[i][col] != '.']
        if mode == 'box':
            rows = [x + (row)//3*3 for x in range(3)] # return [0, 1, 2] if row is 0, 1, or 2, etc...
            cols = [x + (col)//3*3 for x in range(3)] # return [0, 1, 2] if col is 0, 1, or 2, etc...
            return [int(board[i][j]) for i in rows for j in cols if board[i][j] != '.']


    def getPossible(self, line: list) -> list:
        """
        get list of possible numbers a square can be given a row, column, or box
        """
        possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        return list(possible - set(line))

    def getIntersection(self, col: list, row: list, box: list):
        """
        return the list of intersections given the lists of column, row, and box
        """
        return list(set(col) & set(row) & set(box))


    def solveSudoku(self) -> None:
        """
        modify board in-place until board is solved
        """
        # make list of undecided squares (length of possible, row, column, possible candidates)
        undecided = []
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    undecided.append((9, row, col, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
                    
        # while there are items in undecided, keep narrowing possible solutions
        # TODO: make random guess if stuck
        while undecided:
            square = undecided.pop(0)
            row, col = square[1], square[2]
            row_possible = self.getPossible(self.getLineBox(self.board, row, col, 'row'))
            col_possible = self.getPossible(self.getLineBox(self.board, row, col, 'col'))
            box_possible = self.getPossible(self.getLineBox(self.board, row, col, 'box'))
            possible = self.getIntersection(row_possible, col_possible, box_possible)
            if len(possible) == 0:
                print("can't find possible solution for ({}, {})".format(row, col))
                self.displayBoard()
            if len(possible) == 1:
                self.board[row][col] = str(possible[0])
            else:
                # TODO: sort the undecided to speed up without going into 
                undecided.append((len(possible), row, col, possible))
        print("Board solved!")
        self.displayBoard()
####################################################################################################
if __name__ == '__main__':
    sudoku_board = Sudoku([["5","3",".",".","7",".",".",".","."],
                           ["6",".",".","1","9","5",".",".","."],
                           [".","9","8",".",".",".",".","6","."],
                           ["8",".",".",".","6",".",".",".","3"],
                           ["4",".",".","8",".","3",".",".","1"],
                           ["7",".",".",".","2",".",".",".","6"],
                           [".","6",".",".",".",".","2","8","."],
                           [".",".",".","4","1","9",".",".","5"],
                           [".",".",".",".","8",".",".","7","9"]
                           ])
    
    sudoku_board.displayBoard()
    sudoku_board.solveSudoku()
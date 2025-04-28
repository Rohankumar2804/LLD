from typing import List

from ChessGame.enums import Color
from ChessGame.models.piece import Pawn, Bishop,Rook,Knight,Queen,King
from ChessGame.models.position import Cell


class Board:
    size : int
    grid : List[List[Cell]]

    def __init__(self):
        self.size = 8
        self.grid =  [[Cell(row, col) for col in range(self.size)] for row in range(self.size)]
        self.initialize()

    def initialize(self):
        for i in range(self.size):
            self.grid[1][i] = Cell(1,i,Pawn(Color.BLACK))
            self.grid[6][i] = Cell(6,i,Pawn(Color.WHITE))

        order = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        for i,piece in enumerate(order):
            self.grid[0][i] = Cell(0,i, piece(Color.BLACK))
            self.grid[7][i] = Cell(7,i,piece(Color.WHITE))

    def print_board(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

    def get_cell(self,row,col):
        return self.grid[row][col]
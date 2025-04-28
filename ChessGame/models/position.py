from typing import Any


class Cell:
    row: int
    col: int
    piece: Any
    def __init__(self,row,col,piece = None):
        self.row = row
        self.col = col
        self.piece=piece

    def __str__(self):
        return f"{self.piece.symbol}" if self.piece else "."
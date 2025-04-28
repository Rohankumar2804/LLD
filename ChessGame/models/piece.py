from abc import abstractmethod

from ChessGame.enums import Color
from ChessGame.models.position import Cell


class Piece:
    color: str
    def __init__(self,color):
        self.color = color

    @abstractmethod
    def can_move(self,point_1,point_2,board):
         pass

class Pawn(Piece):
    symbol = 'P'

    def can_move(self,point_1: Cell,point_2:Cell,board) -> bool:
        direction = -1 if point_1.piece.color == Color.WHITE else 1
        start_row = 6 if point_1.piece.color == Color.WHITE else 1
        print(direction)
        if point_1.col == point_2.col:
            if point_2.piece:
                return False
            if point_2.row - point_2.row == direction:
                return True
            if point_1.row == start_row and (point_2.row-point_1.row) == 2*direction:
                return  True
        elif (point_2.row-point_1.row) == direction and abs(point_2.col-point_1.col) == 1:
             return  point_2.piece and point_1.piece.color!=point_2.piece.color
        return False



class Rook(Piece):
    symbol = 'R'

    def can_move(self,point_1: Cell,point_2:Cell,board) -> bool:
        return point_1.row == point_2.row or point_2.col == point_1.col

class Knight(Piece):
    symbol = 'N'

    def can_move(self,point_1: Cell,point_2:Cell,board) -> bool:
        dx = abs(point_1.row - point_2.row)
        dy = abs(point_1.col - point_2.col)
        return (dx,dy) in [(1,2),(2,1)]

class Bishop(Piece):
    symbol = 'B'

    def can_move(self,point_1: Cell,point_2:Cell,board) -> bool:
        return abs(point_1.row-point_2.row) == abs(point_1.col - point_2.col)



class Queen(Piece):
    symbol = 'Q'

    def can_move(self,point_1: Cell,point_2:Cell,board) -> bool:
        return Rook(self.color).can_move(point_1,point_2,board) or Bishop(self.color).can_move(point_1,point_2,board)



class King(Piece):
    symbol = 'K'

    def can_move(self,point_1: Cell,point_2:Cell,board) -> bool:
        dx = abs(point_1.row-point_2.row)
        dy = abs(point_1.col-point_2.col)
        return max(dx,dy) == 1






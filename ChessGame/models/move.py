from ChessGame.models.piece import Piece
from ChessGame.models.position import Cell


class Move:
    pieceMoved: Piece
    pieceKilled: Piece | None
    startCell: Cell
    endCell: Cell

    def __init__(self,start_cell,end_cell,piece_moved,piece_killed=None):
        self.pieceMoved = piece_moved
        self.startCell = start_cell
        self.endCell = end_cell
        self.pieceKilled = piece_killed
        
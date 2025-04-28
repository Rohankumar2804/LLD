from enum import Enum

class Color(Enum):
    WHITE = "WHITE"
    BLACK = "BLACK"

class PieceType(Enum):
    KING = "KING"
    QUEEN = "QUEEN"
    BISHOP = "BISHOP"
    KNIGHT = "KNIGHT"
    ROOK = "ROOK"
    PAWN = "PAWN"

class GameStatus(Enum):
    ACTIVE = "ACTIVE"
    CHECKMATE = "CHECKMATE"
    STALEMATE = "STALEMATE"

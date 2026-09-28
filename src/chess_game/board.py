from .piece import Piece
from .position import Position


class Board:
    def position_free(self, position: Position) -> bool:
        pass

    def piece_at(self, position: Position) -> Piece:
        pass

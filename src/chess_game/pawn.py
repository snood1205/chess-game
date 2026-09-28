from .board import Board
from .piece import Piece
from .position import Position


class Pawn(Piece):
    def check_legal_move(self, other: Position, board: Board) -> bool:
        allowable_offset = 2 if self._at_initial_position() else 1
        return (self.position.check_column_difference(other, allowable_offset) and
                board.position_free(other))

    def _at_initial_position(self) -> bool:
        return ((self.color == 'White' and self.position.row == 2) or
                (self.color == 'Black' and self.position.row == 7))

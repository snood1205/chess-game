from chess_game.board import Board
from chess_game.piece import Piece
from chess_game.position import Position


class Pawn(Piece):
    """
    This class defines a pawn in chess. The pawn can move forward one square except for its first
    move where it can optionally move two. It can only take pieces diagonally. There is also a
    the 'en passant' move where the piece moves diagonally behind a piece that moved forward two
    squares. (e.g. 2. ... e5 3. exd6)
    """

    def check_legal_move(self, other: Position, board: Board) -> bool:
        """
        Checks what moves are legal for the pawn. Implementation of abstract method in Piece.

        Parameters:
            other (Position): The other position to check for legal moves.
            board (Board): The current chess board.
        """
        allowable_offset = 2 if self._at_initial_position() else 1
        # Add capturing including en passant
        return self.position.check_column_difference(
            other, allowable_offset
        ) and board.position_free(other)

    def _at_initial_position(self) -> bool:
        return (self.color == 'White' and self.position.row == 2) or (
            self.color == 'Black' and self.position.row == 7
        )

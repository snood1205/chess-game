from typing import Literal

from .board import Board
from .exceptions import PromotionError
from .pieces.pawn import Pawn
from .position import Position

# In standard algebraic notation, this represents kNight, Bishop, Rook, and Queen respectively.
type Promotions = Literal['N', 'B', 'R', 'Q']


class Move:
    def __init__(
        self,
        from_position: Position,
        to_position: Position,
        board: Board,
        promote_to: None | Promotions = None,
    ):
        self._from_position = from_position
        self._to_position = to_position
        self._board = board
        self._is_capture = False  # TODO: define logic
        self._promote_to = promote_to
        self._validate()

    def san(self) -> str:
        # TODO: handle ambiguity such as if rooks are on a1 and h1 where the one from
        # a1 moves to d1, it is shown as Rad1 instead of just Rd1
        """
        Outputs the position on the chess board in standard algebraic notation (SAN).
        :return:
        """
        original_row = self._from_position.row
        if self._promote_to is not None:
            if self._is_capture:
                return f'{original_row}x{self._to_position}={self._promote_to}'
            return f'{self._to_position}={self._promote_to}'
        if self._is_capture:
            return f'{original_row}x{self._to_position}'
        return f'{self._to_position}'

    def _validate(self):
        # Add further validations, currently only validates promote to.
        if self._promote_to is not None:
            if not isinstance(self._board.piece_at(self._from_position), Pawn):
                raise PromotionError(
                    f'The piece at #{self._from_position} is not a pawn, '
                    'so it is ineligible for promotion'
                )

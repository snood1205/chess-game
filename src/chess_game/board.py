from typing import Literal

from .piece import Piece
from .position import Position
from .pieces.bishop import Bishop
from .pieces.king import King
from .pieces.knight import Knight
from .pieces.pawn import Pawn
from .pieces.queen import Queen
from .pieces.rook import Rook


class Board:
    _BACK_RANK_ORDER = (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)
    _COLUMNS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

    def __init__(self):
        self._create_normal_chessboard()

    def position_free(self, position: Position) -> bool:
        return self.piece_at(position) is None

    def piece_at(self, position: Position) -> Piece | None:
        row, column = position.as_indices()
        return self._board[row][column]

    def _create_normal_chessboard(self):
        self._board = [[None] * 8 for _ in range(8)]
        Board._create_back_rank(empty_row=self._board[0], color='Black')
        Board._create_pawn_rank(empty_row=self._board[1], color='Black')
        Board._create_pawn_rank(empty_row=self._board[6], color='White')
        Board._create_back_rank(empty_row=self._board[7], color='White')

    @staticmethod
    def _create_back_rank(empty_row: list[Piece | None], color: Literal['White', 'Black']):
        row = 8 if color == 'Black' else 1
        for index, (piece_class, column) in enumerate(zip(Board._BACK_RANK_ORDER, Board._COLUMNS)):
            empty_row[index] = piece_class(color, position=Position(row, column))

    @staticmethod
    def _create_pawn_rank(empty_row: list[Piece | None], color: Literal['White', 'Black']):
        row = 7 if color == 'Black' else 2
        for index, column in enumerate(Board._COLUMNS):
            empty_row[index] = Pawn(color, position=Position(row, column))

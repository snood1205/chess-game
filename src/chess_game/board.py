from typing import Literal

from .piece import Piece
from .position import Position
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook


class Board:
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

        empty_row[0] = Rook(color, position=Position(row, column='a'))
        empty_row[1] = Knight(color, position=Position(row, column='b'))
        empty_row[2] = Bishop(color, position=Position(row, column='c'))
        empty_row[3] = Queen(color, position=Position(row, column='d'))
        empty_row[4] = King(color, position=Position(row, column='e'))
        empty_row[5] = Bishop(color, position=Position(row, column='f'))
        empty_row[6] = Knight(color, position=Position(row, column='g'))
        empty_row[7] = Rook(color, position=Position(row, column='h'))

    @staticmethod
    def _create_pawn_rank(empty_row: list[Piece | None], color: Literal['White', 'Black']):
        row = 7 if color == 'Black' else 2

        empty_row[0] = Pawn(color, position=Position(row, column='a'))
        empty_row[1] = Pawn(color, position=Position(row, column='b'))
        empty_row[2] = Pawn(color, position=Position(row, column='c'))
        empty_row[3] = Pawn(color, position=Position(row, column='d'))
        empty_row[4] = Pawn(color, position=Position(row, column='e'))
        empty_row[5] = Pawn(color, position=Position(row, column='f'))
        empty_row[6] = Pawn(color, position=Position(row, column='g'))
        empty_row[7] = Pawn(color, position=Position(row, column='h'))

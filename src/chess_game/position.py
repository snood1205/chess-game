from typing import Final, Literal

type Column = Literal['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
type Row = Literal[1, 2, 3, 4, 5, 6, 7, 8]


class Position:
    """
    Defines a position on the chess board.

    Attributes:
        _row (Row): The row (1-8) that the piece is on
        _column (Column): The column (a-h) that the piece is on
    """

    _COLUMN_ORD_OFFSET: Final = ord('a')

    def __init__(self, row: Row, column: Column):
        self._row: Row = row
        self._column: Column = column

    @property
    def row(self) -> Row:
        return self._row

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return False
        return self._row == other._row and self._column == other._column

    def __hash__(self) -> int:
        return hash((self._row, self._column))

    def __str__(self) -> str:
        return f'{self._column}{self._row}'

    def as_indices(self) -> tuple[int, int]:
        row_index = 8 - self._row
        col_index = self._numeric_column()
        return row_index, col_index

    def is_same_row(self, other: Position) -> bool:
        return self._row == other._row

    def check_column_difference(self, other: Position, allowable_difference: int) -> bool:
        difference = abs(self._numeric_column() - other._numeric_column())
        return difference <= allowable_difference

    def _numeric_column(self):
        return ord(self._column) - self._COLUMN_ORD_OFFSET

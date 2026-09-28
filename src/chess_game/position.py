from typing import Final, Literal

type Column = Literal['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
type Row = Literal[1, 2, 3, 4, 5, 6, 7, 8]


class Position:
    _COLUMN_ORD_OFFSET: Final = ord('a')

    def __init__(self, row: Row, column: Column):
        self._row: Row = row
        self._column: Column = column

    @property
    def row(self) -> Row:
        return self._row

    def _numeric_column(self):
        return ord(self._column) - self._COLUMN_ORD_OFFSET

    def is_same_row(self, other: Position) -> bool:
        return self._row == other._row

    def check_column_difference(self, other: Position, allowable_difference: int) -> bool:
        difference = abs(self._numeric_column() - other._numeric_column())
        return difference <= allowable_difference

from abc import ABC, abstractmethod
from typing import Literal

from .board import Board
from .position import Position

class Piece(ABC):
    def __init__(self, color: Literal['White', 'Black'], position: Position):
        self.color = color
        self.position = position

    @abstractmethod
    def check_legal_move(self, other: Position, board: Board) -> bool:
        pass

    @abstractmethod
    def move(self, other: Position, board: Board) -> bool:
        pass

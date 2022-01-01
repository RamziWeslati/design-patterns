from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from .chore.position import Position
from .chore.move import Move
from .utils.display import grid_to_str


@dataclass
class Maze(ABC):
    squares: List[List[bool]]
    start: Position
    target: Position
    SQUARE_LABEL = " "
    NO_SQUARE_LABEL = "■"
    START_LABEL = "♚"
    TARGET_LABEL = "⚑"

    @abstractmethod
    def update_position(self, position: Position, movement: Move) -> Position:
        ...

    @abstractmethod
    def is_legal_position(self, candidate_position: Position) -> bool:
        ...

    def __str__(self) -> str:
        return grid_to_str(self._get_maze_representation())

    def __post_init__(self):
        self._validate_target()
        self.validate()

    @abstractmethod
    def _validate(self):
        ...

    def _validate_target(self):
        if not self.is_legal_position(self.target):
            raise InvalidTargetError

    def _get_maze_representation(self) -> str:
        maze_representation = [
            [self.SQUARE_LABEL if square else self.NO_SQUARE_LABEL for square in line]
            for line in self.squares
        ]
        maze_representation[self.start.y][self.start.x] = self.START_LABEL
        maze_representation[self.target.y][self.target.x] = self.TARGET_LABEL
        return maze_representation


class InvalidTargetError(Exception):
    pass

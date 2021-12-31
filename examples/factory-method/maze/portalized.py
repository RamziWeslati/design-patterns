from dataclasses import dataclass
from typing import Dict
from itertools import chain

from .chore.move import Move, apply_move
from .chore.position import Position
from .maze import Maze

from utils.validation import get_cycles


@dataclass
class PortalMaze(Maze):
    portals: Dict[Position, Position]

    PORTAL_ENTRY_LABEL = "o"
    PORTAL_EXIT_LABEL = "->"
    PORTAL_ENTRY_N_EXIT = "o->"

    def update_position(self, position: Position, movement: Move) -> Position:
        updated_position = apply_move(position, movement)

        if not self.is_legal_position(updated_position):
            return position
        if self.is_portal(updated_position):
            return self._teleport(position)
        return updated_position

    def is_legal_position(self, position: Position) -> bool:
        if self._is_out_of_bounderies(position):
            return False

        return self.squares[position.y][position.x]

    def is_portal(self, position: Position):
        return position in self.portals.keys()

    def _is_portal_exit(self, position: Position):
        return position in self.portals.values()

    def _teleport(self, position: Position):
        if self.is_portal(position) and self._is_portal_exit(position):
            # validation insures that there is no infinite telportation
            return self._teleport(position)

        if self.is_portal(position):
            return self.portals[position]

        raise NoPortalError

    def _is_out_of_bounderies(self, position: Position):
        x, y = position.x, position.y
        if x < 0 or y < 0:
            return True
        if y >= len(self.squares) or x >= len(self.squares[y]):
            return True
        return False

    def _get_maze_representation(self):
        maze_representation = super()._get_maze_representation()

        for line, y in enumerate(self.squares):
            for x in range(len(line)):
                _position = Position(x, y)
                if self.is_portal(_position) and self._is_portal_exit(_position):
                    maze_representation[y][x] = self.PORTAL_ENTRY_N_EXIT
                elif self.is_portal(_position):
                    maze_representation[y][x] = self.PORTAL_ENTRY_LABEL
                elif self._is_portal_exit(_position):
                    maze_representation[y][x] = self.PORTAL_EXIT_LABEL

        return maze_representation

    def _validate_no_portal_cycles(self):
        found_cycles = get_cycles(self.portals)
        if found_cycles:
            raise PortalCycleError

    def _validate_portals_are_squares(self):
        for portal in set(chain(*self.portals.items())):
            x, y = portal
            if not self.squares[x][y]:
                raise InvalidPortalError

    def _validate(self):
        self._validate_portals_are_squares()
        self._validate_no_portal_cycles()


class NoPortalError(Exception):
    pass


class PortalCycleError(Exception):
    pass


class InvalidPortalError(Exception):
    pass

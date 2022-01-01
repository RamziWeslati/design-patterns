from .maze import Maze
from .chore.position import Position
from .chore.move import Move, apply_move


class StandardMaze(Maze):
    def update_position(self, position: Position, movement: Move) -> Position:
        updated_position = apply_move(position, movement)

        if self.is_legal_position(updated_position):
            return updated_position
        return position

    def is_legal_position(self, position: Position) -> bool:
        if self._is_out_of_bounderies(position):
            return False

        return self.squares[position.y][position.x]

    def _is_out_of_bounderies(self, position: Position):
        x, y = position.x, position.y
        return x < 0 or y < 0 or y >= len(self.squares) or x >= len(self.squares[y])

    def _validate(self):
        pass


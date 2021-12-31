from .position import Position

class Move:
    LEFT, RIGHT, UP, DOWN = range(4)

def apply_move(position: Position, move: Move):
    match move:
        case Move.LEFT:
            updated_position = Position(x=position.x - 1, y=position.y)
        case Move.RIGHT:
            updated_position = Position(x=position.x + 1, y=position.y)
        case Move.UP:
            updated_position = Position(x=position.x, y=position.y - 1)
        case Move.DOWN:
            updated_position = Position(x=position.x, y=position.y + 1)
        case _:
            raise IllegalMoveError
    
    return updated_position

class IllegalMoveError(Exception):
    pass

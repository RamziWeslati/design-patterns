from dataclasses import dataclass


@dataclass
class Position:
    y: int
    x: int

    def __key(self):
        return (self.x, self.y)

    def __eq__(self, other: object):
        if isinstance(other, Position):
            return self.__key() == other.__key()

        raise NotImplementedError

    def __hash__(self):
        return hash(self.__key())

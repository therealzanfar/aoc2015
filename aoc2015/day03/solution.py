"""AOC 2015 Day 3 solutions."""

from typing import NamedTuple, Optional


class Coord(NamedTuple):
    """Coordinate."""

    x: int
    y: int

    def __add__(self, other: "Coord") -> "Coord":
        return self.__class__(self.x + other.x, self.y + other.y)


DIRECTIONS: dict[str, Coord] = {
    "<": Coord(-1, 0),
    ">": Coord(1, 0),
    "^": Coord(0, 1),
    "v": Coord(0, -1),
}


def part_a_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    pos = Coord(0, 0)
    visited: set[Coord] = {pos}

    for direction in input_:
        move = DIRECTIONS[direction]
        pos += move
        visited.add(pos)

    return len(visited)


def part_b_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part B input."""
    positions: dict[int, Coord] = {
        0: Coord(0, 0),
        1: Coord(0, 0),
    }
    visited: set[Coord] = {positions[0], positions[1]}
    mover = 0

    for direction in input_:
        move = DIRECTIONS[direction]
        positions[mover] += move
        visited.add(positions[mover])

        mover = (mover + 1) % len(positions)

    return len(visited)

"""AOC 2015 Day 1 solutions."""

from typing import Optional


def part_a_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    floor = 0

    for c in input_:
        if c == "(":
            floor += 1

        elif c == ")":
            floor -= 1

        else:
            raise ValueError(f"Unknown input character: {c}")

    return floor


def part_b_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    floor = 0

    for x, c in enumerate(input_):
        if c == "(":
            floor += 1

        elif c == ")":
            floor -= 1

        else:
            raise ValueError(f"Unknown input character: {c}")

        if floor == -1:
            return x + 1

    raise ValueError(f"Sequence never reached -1 in {x} elements")

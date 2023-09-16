"""Generic puzzle input code."""

import importlib.resources
from typing import NamedTuple

import aoc2015

YEAR = 2015

DAY_COUNT_MIN = 1
DAY_COUNT_MAX = 25
DAY_SUBMODULE_FMT = "day{:02d}"

PUZZLE_INPUT_FILENAME = "input.data"


class Example(NamedTuple):
    """Puzzle solution example."""

    input: str  # noqa: A003
    solution: int


def get_puzzle_input(day: int) -> str:
    """Extract that day's input and return it as a string."""
    puzzle_input_path = (
        importlib.resources.files(
            getattr(aoc2015, DAY_SUBMODULE_FMT.format(day)),
        )
        / PUZZLE_INPUT_FILENAME
    )

    with puzzle_input_path.open("rt", encoding="utf-8") as input_fh:
        return input_fh.read().strip()

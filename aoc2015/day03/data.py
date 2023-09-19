"""AOC 2015 Day 3 example data and input functions."""

from aoc2015.data import Example, get_puzzle_input

# Adding examples to a part's list signals to the system that the part is
# ready for testing

PART_A_EXAMPLES: list[Example] = [
    Example(">", 2),
    Example("^>v<", 4),
    Example("^v^v^v^v^v", 2),
]

PART_B_EXAMPLES: list[Example] = [
    Example("^v", 3),
    Example("^>v<", 3),
    Example("^v^v^v^v^v", 11),
]

PUZZLE_INPUT = get_puzzle_input(3)

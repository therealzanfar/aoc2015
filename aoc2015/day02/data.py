"""AOC 2015 Day 2 example data and input functions."""

from aoc2015.data import Example, get_puzzle_input

# Adding examples to a part's list signals to the system that the part is
# ready for testing

PART_A_EXAMPLES: list[Example] = [
    Example("2x3x4", 58),
    Example("1x1x10", 43),
    Example("2x3x4\n1x1x10", 58 + 43),
]

PART_B_EXAMPLES: list[Example] = [
    Example("2x3x4", 34),
    Example("1x1x10", 14),
    Example("2x3x4\n1x1x10", 34 + 14),
]

PUZZLE_INPUT = get_puzzle_input(2)

"""AOC 2015 Day 4 example data and input functions."""

from aoc2015.data import Example, get_puzzle_input

# Adding examples to a part's list signals to the system that the part is
# ready for testing

PART_A_EXAMPLES: list[Example] = [
    Example("abcdef", 609043),
    Example("pqrstuv", 1048970),  # cSpell:words pqrstuv
]

PART_B_EXAMPLES: list[Example] = [
    Example("abcdef", 6742839),
    Example("pqrstuv", 5714438),  # cSpell:words pqrstuv
]

PUZZLE_INPUT = get_puzzle_input(4)

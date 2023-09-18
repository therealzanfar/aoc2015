"""AOC 2015 Day 1 example data and input functions."""

from aoc2015.data import Example, get_puzzle_input

# Adding examples to a part's list signals to the system that the part is
# ready for testing

PART_A_EXAMPLES: list[Example] = [
    Example("(())", 0),
    Example("()()", 0),
    Example("(((", 3),
    Example("(()(()(", 3),
    Example("))(((((", 3),
    Example("())", -1),
    Example("))(", -1),
    Example(")))", -3),
    Example(")())())", -3),
]

PART_B_EXAMPLES: list[Example] = [
    Example(")", 1),
    Example("()())", 5),
]

PUZZLE_INPUT = get_puzzle_input(1)

"""AOC 2015 Day 5 example data and input functions."""

from aoc2015.data import Example, get_puzzle_input

# Adding examples to a part's list signals to the system that the part is
# ready for testing

# cSpell:disable
PART_A_EXAMPLES: list[Example] = [
    Example("ugknbfddgicrmopn", 1),
    Example("aaa", 1),
    Example("jchzalrnumimnmhp", 0),
    Example("haegwjzuvuyypxyu", 0),
    Example("dvszwmarrgswjxmb", 0),
]

PART_B_EXAMPLES: list[Example] = [
    Example("qjhvhtzxzqqjkmpb", 1),
    Example("xxyxx", 1),
    Example("uurcxstgmygtbstg", 0),
    Example("ieodomkazucvgmuy", 0),
]
# cSpell:enable

PUZZLE_INPUT = get_puzzle_input(5)

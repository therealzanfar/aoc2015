"""AOC 2015 Day 5 solutions."""

from collections import Counter
from typing import Optional


class StringWindow:
    """String windowing class."""

    def __init__(self, size: int = 2, default: str = " ") -> None:
        self._size = size
        self._data = [default[0] for _ in range(size)]

    def push(self, value: str) -> None:
        """Push a value into the Window."""
        self._data[0 : self._size - 1] = self._data[1:]
        self._data[-1] = value

    @property
    def value(self) -> str:
        """Extract the windowed value."""
        return "".join(self._data)


def is_nice_a(string: str) -> bool:
    """Compute the niceness according to part A."""
    pair = StringWindow(2)

    vowels = 0
    has_pair = False

    for c in string:
        pair.push(c)

        if c in "aeiou":  # cSpell:words aeiou
            vowels += 1

        if pair.value[0] == pair.value[1]:
            has_pair = True

        if pair.value in ("ab", "cd", "pq", "xy"):
            return False

    return vowels >= 3 and has_pair  # noqa: PLR2004


def is_nice_b(string: str) -> bool:
    """Compute the niceness according to part B."""
    pair = StringWindow(2)
    triple = StringWindow(3)
    last_pair_found: Optional[str] = None

    pair_counts = Counter()
    has_triple = False

    for c in string:
        pair.push(c)
        triple.push(c)

        if pair.value[0] == pair.value[1]:
            if pair.value[0] != last_pair_found:
                pair_counts[pair.value] += 1
                last_pair_found = pair.value[0]
            else:
                # Else, we skip the pair as it's a triple
                # but we still reset for next time
                last_pair_found = None
        else:
            pair_counts[pair.value] += 1
            last_pair_found = None

        if triple.value[0] == triple.value[2]:
            has_triple = True

        if (
            has_triple
            and pair_counts
            and pair_counts.most_common(1)[0][1] >= 2  # noqa: PLR2004
        ):
            return True

    return False


def part_a_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    return sum(int(is_nice_a(candidate)) for candidate in input_.splitlines())


def part_b_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part B input."""
    return sum(int(is_nice_b(candidate)) for candidate in input_.splitlines())

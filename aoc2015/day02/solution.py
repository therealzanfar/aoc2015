"""AOC 2015 Day 2 solutions."""

from typing import NamedTuple, Optional


class PresentSpec(NamedTuple):
    """Details of a present."""

    l: int  # noqa: E741
    w: int
    h: int

    @classmethod
    def parse(cls, data: str) -> "PresentSpec":
        """Parse a spec from a string."""
        return cls(*(int(s) for s in data.lower().split("x")))


def part_a_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    total_paper = 0

    for present_data in input_.splitlines():
        p = PresentSpec.parse(present_data)
        side_areas = (p.l * p.w, p.w * p.h, p.l * p.h)
        present_area = 2 * sum(side_areas) + min(side_areas)

        total_paper += present_area

    return total_paper


def part_b_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part B input."""
    total_ribbon = 0

    for present_data in input_.splitlines():
        p = PresentSpec.parse(present_data)
        dims = sorted((p.l, p.w, p.h))

        present_ribbon = 2 * dims[0] + 2 * dims[1] + dims[0] * dims[1] * dims[2]
        total_ribbon += present_ribbon

    return total_ribbon

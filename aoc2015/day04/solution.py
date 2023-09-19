"""AOC 2015 Day 4 solutions."""

from hashlib import md5
from typing import Optional


def part_a_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part A input."""
    key = input_
    salt = 0

    key_hash = md5(key.encode("utf-8"))

    while True:
        hashed = key_hash.copy()
        hashed.update(str(salt).encode("utf-8"))

        if hashed.hexdigest().startswith("00000"):
            return salt

        salt += 1

        if salt > 10**10:
            break

    return None


def part_b_solution(input_: str) -> Optional[int]:
    """Compute the solution to a Part B input."""
    key = input_
    salt = 0

    key_hash = md5(key.encode("utf-8"))

    while True:
        hashed = key_hash.copy()
        hashed.update(str(salt).encode("utf-8"))

        if hashed.hexdigest().startswith("000000"):
            return salt

        salt += 1

        if salt > 10**10:
            break

    return None

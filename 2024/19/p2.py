"""Advent of Code 2014 - Day 19 Part 2"""
import sys
from functools import cache

from p1 import parse_input

# Just in case
sys.setrecursionlimit(100000)


@cache
def count(design: str) -> bool:
    """Count how many ways the given design can be constructed from the
    available designs.

    Parameters
    ----------
    design: str
        Desired design to construct.

    Returns
    -------
    int
        Number of ways the design can be constructed.
    """
    if not design:
        return 1

    result = 0
    for p in patterns:
        if design.startswith(p):
            result += count(design[len(p):])

    return result


if __name__ == '__main__':
    patterns, designs = parse_input()
    print(f'Part 2 Answer: {sum([count(d) for d in designs])}')

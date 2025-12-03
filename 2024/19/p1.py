"""Advent of Code 2014 - Day 19 Part 1"""
from functools import cache
from pathlib import Path


def parse_input(f_path: str = 'input.txt') -> tuple[list[str], list[str]]:
    """Return input from a file and return as a list of tuples.

    Parameters
    ----------
    f_path: str, optional
        Path of the input file to read. Default is 'input.txt'.

    Returns
    -------
    tuple of list of str
        Parsed designs and patterns.
    """
    patterns, designs = Path(f_path).read_text().split('\n\n')
    return patterns.strip().split(', '), [x for x in designs.split('\n') if x]


@cache
def count(design: str) -> int:
    """Determine if the given design can be constructed from the available
    patterns.

    Parameters
    ----------
    design: str
        Desired design to construct.

    Returns
    -------
    int
        1 if the design can be constructed, else None.
    """
    if not design:
        return 1

    return sum(
        count(design[len(p):]) for p in patterns if design.startswith(p))


if __name__ == '__main__':
    patterns, designs = parse_input()

    num_combos = len([c for c in [count(d) for d in designs] if c])
    print(f'Part 1 Answer: {num_combos}')

"""Advent of Code 2024 - Day 1 Part 2"""
from collections import Counter

from p1 import parse_input


def solve(list1: list[int], list2: list[int]) -> int:
    """Solution to Part 2.

    Parameters
    ----------
    list1: list of int
    list2: list of int

    Returns
    -------
    int
    """
    sum = 0
    list2_count = Counter(list2)

    for x in list1:
        if x in list2_count:
            sum += x * list2_count[x]

    return sum


if __name__ == '__main__':
    print(f'Day 01 Part 2 answer: {solve(*parse_input())}')

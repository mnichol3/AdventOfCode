"""Advent of Code 2024 - Day 7 Part 2"""
import re
from itertools import product
from operator import add, mul

from p1 import parse_input


def concat(a: int, b: int) -> int:
    """Concatenate two integers."""
    return int(f'{a}{b}')


def part2(calibrations: list[str]) -> int:
    """Solution to Part 2.

    Parameters
    ----------
    calibrations: list of str

    Returns
    -------
    int
        Calibration results.

    Problem
    -------
    * Each line is a single equation.
    * Numbers can either be multiplied or added to equal the test value.
    * Operators are always evaluated left to right.
    * We now have the concetenation operator.

    Walkthrough
    -----------
    * Same approach as in Part 1.
    """
    valid_sum = 0
    for line in calibrations:
        nums = [int(x) for x in re.findall(r'\d+', line)]

        test_val = nums[0]
        operands = nums[1:]

        for combo in product([add, mul, concat], repeat=len(operands)-1):
            total = operands[0]
            for i in range(len(combo)):
                total = combo[i](total, operands[i+1])

            if total == test_val:
                valid_sum += test_val
                break

    return valid_sum


if __name__ == '__main__':
    print(f'Day 07 Part 2 answer: {part2(parse_input())}')

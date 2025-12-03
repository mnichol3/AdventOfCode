"""Advent of Code 2024 - Day 7 Part 1"""
import re
from itertools import product
from operator import add, mul
from pathlib import Path


def parse_input(fname: str = None) -> list[str]:
    """Parse the input from a text file.

    Parameters
    ----------
    None.

    Returns
    -------
    list of str
    """
    fname = 'input.txt' if fname is None else fname

    return [x for x in Path(fname).read_text().split('\n') if x]


def part1(calibrations: list[str]) -> int:
    """Solution to Part 1.

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

    Walkthrough
    -----------
    * Split each line into its test value and operands.
    * Brute force lol
    """
    valid_sum = 0
    for line in calibrations:
        nums = [int(x) for x in re.findall(r'\d+', line)]

        test_val = nums[0]
        operands = nums[1:]

        for combo in product([add, mul], repeat=len(operands)-1):
            total = operands[0]
            for i in range(len(combo)):
                total = combo[i](total, operands[i+1])

            if total == test_val:
                valid_sum += test_val
                break

    return valid_sum


if __name__ == '__main__':
    print(f'Day 07 Part 1 answer: {part1(parse_input())}')

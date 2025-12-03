"""Advent of Code 2024 - Day 3 Part 1"""
import re
from pathlib import Path


def parse_input() -> list[str]:
    """Parse the input from a text file.

    Parameters
    ----------
    None.

    Returns
    -------
    list of list of str
    """
    return [x for x in Path('input.txt').read_text().split('\n') if x]


def answer(instructions: list[str]) -> int:
    """Compute the answer for Part 1.

    Parameters
    ----------
    instructions: list of str
        Instructions to parse.

    Returns
    -------
    int
        Sum of valid multiplication instructions.
    """
    total = 0
    patt = re.compile(r'mul\((\d{1,3})\,(\d{1,3})\)')

    for instr in instructions:
        valid = patt.findall(instr)

        for x in valid:
            total += int(x[0]) * int(x[1])

    return total


if __name__ == '__main__':
    print(f'Day 03 Part 1 answer: {answer(parse_input())}')

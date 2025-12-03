"""Advent of Code 2024 - Day 21 Part 1"""
from enum import Enum
from operator import sub
from pathlib import Path


def parse_input(f_path = 'input.txt') -> list[str]:
    """Parse input from file.

    Parameters
    ----------
    f_path: str, optional
        Input file path. Default is 'input.txt'.

    Returns
    -------
    list of str
    """
    return [x for x in Path(f_path).read_text().split('\n') if x]


def dist(numer1: int, numer2: int) -> int:
    abs(numer1[0]-numer2[0]) + abs(numer1[1]-numer2[1])


def get_dir_keys(inp: tuple[int, int]) -> str:
    keys = ''
    if inp[0] < 0:
        keys += 'v' * abs(inp[0])
    else:
        keys += 'v' * inp[0]

    if inp[1] < 0:
        keys += '<' * abs(inp[1])
    else:
        keys += '>' * inp[1]

    return keys


def subtract(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return tuple(map(sub, a, b))


directional_pad = {
    'A': (0, 2),
    'UP': (0, 1),
    'LEFT': (1, 0),
    'DOWN': (1, 1),
    'RIGHT': (1, 2),
}


numeric_pad = {
    7: (0, 0),
    8: (0, 1),
    9: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    0: (3, 1),
    'A': (3, 2),
}


for code in codes:
    pointer1 = directional_pad['A']
    pointer2 = directional_pad['A']
    numeric_pointer = numeric_pad['A']
    keys = ''

    for c in code:
        try:
            c = int(c)
        except TypeError:
            pass

        next1 = directional_pad[c]
        delta1 = subtract(next1, pointer1)

        keys += get_dir_keys(delta1) + 'A'





if __name__ == '__main__':
    codes = parse_input('example.txt')

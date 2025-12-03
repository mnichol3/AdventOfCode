"""Advent of Code 2024 - Day 9 Part 1"""
from pathlib import Path


def parse_input(fname: str = 'input.txt') -> list[int]:
    """Parse the input from a text file.

    Parameters
    ----------
    fname: str, optional
        Input filename. Default is 'input.txt'.

    Returns
    -------
    list of list of int
    """
    return [int(x) for x in Path(fname).read_text().strip('\n')]


def part1(disk: list[int]) -> int:
    """Solution to Part 1.

    Parameters
    ----------
    list of list of int

    Returns
    -------
    int
    """
    mem_map = []
    file_id = 0

    for i, x in enumerate(disk):
        if i % 2 == 0:
            mem_map.extend([file_id for _ in range(x)])
            file_id += 1
        else:
            mem_map.extend(['.' for _ in range(x)])

    j = len(mem_map) - 1
    i = 0
    while i != j:
        if mem_map[i] == '.':
            while mem_map[j] == '.':
                j -= 1

            mem_map[i] = mem_map[j]
            mem_map[j] = '.'
            j -= 1
        i += 1

    sum = 0
    for i, x in enumerate(mem_map):
        if x != '.':
            sum += i * x

    return sum


if __name__ == '__main__':
    print(f'Day 09 Part 1 answer: {part1(parse_input())}')

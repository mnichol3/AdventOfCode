"""Advent of Code 2024 - Day 8 Part 2"""
from collections import defaultdict
from itertools import combinations

from p1 import parse_input


def part2(grid: list[list[str]]) -> int:
    """Solution to Part 2.

    Parameters
    ----------
    grid: list of list of str

    Returns
    -------
    int
    """
    locations = defaultdict(set)
    ni, nj = len(grid), len(grid[0])

    for i in range(ni):
        for j in range(nj):
            if grid[i][j] != '.':
                locations[grid[i][j]].add((i, j))

    antinodes = set()
    for loc in locations.values():
        for (a, b), (c, d) in combinations(loc, 2):
            di = a - c
            dj = b - d

            row, col = a, b
            while row in range(ni) and col in range(nj):
                antinodes.add((row, col))
                row += di
                col += dj

            row, col = c, d
            while row in range(ni) and col in range(nj):
                antinodes.add((row, col))
                row -= di
                col -= dj

    return len(antinodes)


if __name__ == '__main__':
    print(f'Day 08 Part 2 answer: {part2(parse_input())}')

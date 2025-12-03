"""Advent of Code 2024 - Day 14 Part 1"""
import re
from math import prod
from pathlib import Path


TuplePair = tuple[int, int]


def parse_input(fpath: str = 'input.txt') -> list[tuple[TuplePair]]:
    """Parse and return input."""
    patt = re.compile(r'(-?\d{1,3})\,(-?\d{1,3})')
    robots = []

    for x in Path(fpath).read_text().split('\n'):
        if x == '' or x == '\n':
            continue

        match = patt.findall(x)
        pos = tuple(map(int, match[0]))
        vel = tuple(map(int, match[1]))

        robots.append((pos, vel))

    return robots


def part1() -> int:
    """Solution to Part 1."""
    nx = 101
    ny = 103
    nt = 100
    hx = nx // 2
    hy = ny // 2

    quads = [0, 0, 0, 0]

    for pos, vel in parse_input():
        x, y = pos
        dx, dy = vel

        x = (x + dx*nt) % nx
        y = (y + dy*nt) % ny

        if x == hx or y == hy:
            continue

        quad_idx = (int(x > hx)) + (int(y > hy) * 2)
        quads[quad_idx] += 1

    return prod(quads)


if __name__ == '__main__':
    print(f'Part 1 answer: {part1()}')

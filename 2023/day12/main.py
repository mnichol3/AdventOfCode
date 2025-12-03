"""
Advent of Code 2023
Day 12 - Hot Springs
"""
from pathlib import Path


SAMPLE_INP = [
    '???.### 1,1,3',
    '.??..??...?##. 1,1,3',
    '?#?#?#?#?#?#?#? 1,3,1,6',
    '????.#...#... 4,1,1',
    '????.######..#####. 1,6,5',
    '?###???????? 3,2,1',
]


def explode(input: list[str]) -> list[list[str]]:
    return [list(x) for x in input]


def solve_1(grid: list[list[str]]) -> int:
    """Solution for Part 1."""
    raise NotImplementedError


def solve_2(grid: list[list[str]]) -> int:
    """Solution for Part 2."""
    raise NotImplementedError


def test_1() -> None:
    """Unit test for Part 1 solution."""
    soln = solve_1(explode(SAMPLE_INP))
    assert soln == 21, f'{soln} != 21'

    print('Test 1 OK')


if __name__ == '__main__':
    #grid = Path(__file__).with_name('input.txt').read_text().readlines()
    grid = explode(SAMPLE_INP)
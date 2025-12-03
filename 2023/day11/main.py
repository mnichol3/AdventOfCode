"""
Advent of Code 2023
Day 11 - Cosmic Expansion
"""
from pathlib import Path


SAMPLE_INP = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....',
]


SAMPLE_INP_EXP = [
    '....#........',
    '.........#...',
    '#............',
    '.............',
    '.............',
    '........#....',
    '.#...........',
    '............#',
    '.............',
    '.............',
    '.........#...',
    '#....#.......',
]


def explode(grid: list[str]) -> list[list[str]]:
    return [list(x) for x in grid]


def solve(grid: list[list[str]], incr: int = 2) -> int:
    """Solution to Parts 1 & 2"""
    visited = []
    distances = []

    empty_rows = [idx for idx, row in enumerate(grid) if set(row) == {'.'}]
    empty_cols = [x for x in range(len(grid[0])) if set([y[x] for y in grid]) == {'.'}]

    coords = [(i, j) for i, row in enumerate(grid) for j, ele \
               in enumerate(row) if ele == '#']

    for idx, coord in enumerate(coords):
        i, j = coord

        i += len([x for x in empty_rows if x < i]) * (incr - 1)
        j += len([y for y in empty_cols if y < j]) * (incr - 1)

        coords[idx] = (i, j, idx + 1)

    for idx, origin in enumerate(coords):
        for dest in coords[idx:]:
            path = f'{origin[2]}-{dest[2]}'
            if path not in visited:
                distances.append(
                    abs(dest[0] - origin[0]) + abs(dest[1] - origin[1])
                )
                visited.append(path)

    return sum(distances)


def test_1() -> None:
    """Simple unit test for Part 1 solution."""
    soln = solve_1(explode(SAMPLE_INP))
    assert soln == 374, f'{soln} != 374'

    print('Test 1 OK')


def test_2() -> None:
    """Simple unit test for Part 2 solution."""
    inp = explode(SAMPLE_INP)
    soln = solve_2(inp, incr=10)
    assert soln == 1030, f'{soln} != 1030'

    soln = solve_2(inp, incr=100)
    assert soln == 8410, f'{soln} != 8410'

    print('Test 2 OK')


if __name__ == '__main__':
    inp = explode(Path(__file__).with_name('input.txt').read_text().splitlines())

    # Part 1 solution
    #soln = solve(inp)

    # Part 2 solution
    soln = solve(inp, incr=1000000)

    print(soln)

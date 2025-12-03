"""
Advent of Code 2023
Day 18 - Lavaduct Lagoon
"""
from pathlib import Path


SAMPLE_GRID = [
    'R 6 (#70c710)',
    'D 5 (#0dc571)',
    'L 2 (#5713f0)',
    'D 2 (#d2c081)',
    'R 2 (#59c680)',
    'D 2 (#411b91)',
    'L 5 (#8ceee2)',
    'U 2 (#caa173)',
    'L 1 (#1b58a2)',
    'U 2 (#caa171)',
    'R 2 (#7807d2)',
    'U 3 (#a77fa3)',
    'L 2 (#015232)',
    'U 2 (#7a21e3)',
]


DIG_DIR = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
}


def explode(grid: list[str]) -> list[list[str]]:
    return [x.split(' ') for x in grid]


def solve_1(instructions: list[str]) -> int:
    """Solution to Part 1."""
    instructions = explode(instructions)

    holes = [(0, 0)]

    for idx, step in enumerate(instructions):
        move = DIG_DIR[step[0]]
        num_holes = int(step[1])
        prev_point = holes[idx]

        for n in range(1, num_holes + 1, 1):
            next_i = prev_point[0] + (move[0] * n)
            next_j = prev_point[1] + (move[1] * n)

            holes.append((next_i, next_j))

    ii, jj = zip(*holes)
    i_min = min(ii)
    j_min = min(jj)

    if i_min < 0 or j_min < 0:
        i_offset = abs(i_min) if i_min < 0 else 0
        j_offset = abs(j_min) if j_min < 0 else 0

        holes = [(x[0] + i_offset, x[1] + j_offset) for x in holes]

    n_rows = max(ii)
    n_cols = max(jj)

    print(holes)
    print(n_rows)
    print(n_cols)

    grid = [
        ['#' if (i, j) in holes else '.' for j in range(n_cols + 1)] \
            for i in range(n_rows + 1)
    ]

    for x in grid:
        print(x)
    #for h in holes:
    #    grid[h[0]][h[1]] = '#'





solve_1(SAMPLE_GRID)


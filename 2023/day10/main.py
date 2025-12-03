"""
Advent of Code 2023
Day 10 - Pipe Maze
"""
from pathlib import Path


SAMPLE_INP_1 = [
    '.....',
    '.S-7.',
    '.|.|.',
    '.L-J.',
    '.....',
]


SAMPLE_INP_2 = [
    '..F7.',
    '.FJ|.',
    'SJ.L7',
    '|F--J',
    'LJ...',
]


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


MAPPING = {
    '|': [NORTH, SOUTH],
    '-': [EAST, WEST],
    'L': [NORTH, EAST],
    'J': [NORTH, WEST],
    '7': [SOUTH, WEST],
    'F': [SOUTH, EAST],
}


def get_input(fname: str = 'input.txt') -> list[list[str]]:
    """
    Read input from a text file and return it as nested lists of strings.

    Parameters
    ----------
    fname: str, optional
        Name of the file to read.
        Default is 'input.txt'.

    Returns
    -------
    list of lists of strings.

    Raises
    ------
    FileNotFoundError
    """
    raw = Path(__file__).with_name(fname).read_text().splitlines()

    return [list(x) for x in raw]


def find_start(inp: list[list[str]]) -> tuple[float]:
    """
    Get the coordinates of the start point.

    Parameters
    ----------
    inp: list of list of str

    Returns
    -------
    tuple of float
    """
    coord = (0, 0)
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == 'S':
                coord = (i, j)

    return coord


def solve_1(grid: list[list[float]]) -> int:
    """
    Solution to Part 1.

    Parameters
    ----------
    grid: list of list of floats
        Input array.

    Returns
    -------
    int
    """
    path = []
    start_i, start_j = find_start(grid)
    grid[start_i][start_j] = 'F'
    curr_pt = (start_i, start_j, 'F')

    while curr_pt not in path:
        path.append(curr_pt)
        moves = MAPPING[curr_pt[2]]

        for m in moves:
            n_i = curr_pt[0] + m[0]
            n_j = curr_pt[1] + m[1]

            try:
                n_tile = grid[n_i][n_j]
            except IndexError:
                pass
            else:
                next_pt = (n_i, n_j, n_tile)
                if next_pt not in path:
                    curr_pt = next_pt
                    break

    return int(len(path) / 2)


def solve_2(inp):
    """
    Solution to Part 2.

    Parameters
    ----------


    Returns
    -------

    """
    raise NotImplementedError


if __name__ == '__main__':
    #inp = [list(x) for x in SAMPLE_INP_1]
    inp = get_input()

    print(solve_1(inp))

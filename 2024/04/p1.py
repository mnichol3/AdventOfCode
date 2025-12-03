"""Advent of Code 2024 - Day 4 Part 1"""
from pathlib import Path


def parse_input(fname: str = None) -> list[str]:
    """Parse the input from a text file.

    Parameters
    ----------
    None.

    Returns
    -------
    list of list of str
    """
    fname = 'input.txt' if fname is None else fname

    return [x for x in Path(fname).read_text().split('\n') if x]


def count_matches(puzzle, m, n):
    num = 0
    if puzzle[m][n] != 'X':
        return 0

    row_len = len(puzzle[m])
    pzl_len = len(puzzle)

    if n + 3 < row_len and ''.join(puzzle[m][n+i] for i in range(4)) == 'XMAS':
        # Forward along row
        num += 1
    if n - 3 >= 0 and ''.join(puzzle[m][n-i] for i in range(4)) == 'XMAS':
        # Backward along row
        num += 1
    if m + 3 < pzl_len and ''.join(puzzle[m+i][n] for i in range(4)) == 'XMAS':
        # Downward along column
        num += 1
    if m - 3 >= 0 and ''.join(puzzle[m-i][n] for i in range(4)) == 'XMAS':
        # Upward along column
        num += 1
    if (
        m + 3 < pzl_len and n + 3 < row_len and
        ''.join(puzzle[m+i][n+i] for i in range(4)) == 'XMAS'
    ):
        # Downward along column, forward along row
        num += 1
    if (
        m + 3 < pzl_len and n - 3 >= 0 and
        ''.join(puzzle[m+i][n-i] for i in range(4)) == 'XMAS'
    ):
        # Downward along column, backward along row
        num += 1
    if (
        m - 3 >= 0 and n + 3 < row_len and
        ''.join(puzzle[m-i][n+i] for i in range(4)) == 'XMAS'
    ):
        # Upward along column, forward along row
        num += 1
    if (
        m - 3 >= 0 and n - 3 >= 0 and
        ''.join(puzzle[m-i][n-i] for i in range(4)) == 'XMAS'
    ):
        # Upward along column, backward along row
        num += 1

    return num


def part1(puzzle: list[str]) -> int:
    n = 0

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            n += count_matches(puzzle, i, j)

    return n


if __name__ == '__main__':
    print(f'Day 04 Part 1 answer: {part1(parse_input())}')

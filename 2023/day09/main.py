"""
Advent of Code 2023
Day 9 - Mirage Maintenance
"""
from pathlib import Path


SAMPLE_INPUT = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45],
]


def read_input(fname: str = 'input.txt') -> list[list[float]]:
    """
    Read input from a text file and return it as nested lists of ints.

    Parameters
    ----------
    fname: str, optional
        Name of the file to read.
        Default is 'input.txt'.

    Returns
    -------
    list of lists of ints.
    Ex:
        [
            [0, 3, 6, 9, 12, 15],
            [1, 3, 6, 10, 15, 21],
            [10, 13, 16, 21, 30, 45],
        ]

    Raises
    ------
    FileNotFoundError
    """
    input = Path(__file__).with_name(fname).read_text().splitlines()

    input = [[int(y) for y in x.split()] for x in input]

    return input


def solve_1(hist: list[float]) -> float:
    """
    Solution for Part 1.

    Parameters
    ----------
    hist: list of float

    Return
    ------
    float
    """
    diffs = [hist]
    row_idx = 0

    while list(set(diffs[-1])) != [0]:
        diffs.append(
            [
                diffs[row_idx][idx + 1] - val for idx, val in enumerate(
                    diffs[row_idx][:-1]
                )
            ]
        )
        row_idx += 1

    return sum([x[-1] for x in diffs])


def solve_2(hist: list[float]) -> float:
    """
    Solution for Part 2.

    Parameters
    ----------
    hist: list of float

    Return
    ------
    float
    """
    diffs = [hist]
    row_idx = 0

    while list(set(diffs[-1])) != [0]:
        diffs.append(
            [
                diffs[row_idx][idx + 1] - val for idx, val in enumerate(
                    diffs[row_idx][:-1]
                )
            ]
        )
        row_idx += 1

    val = 0
    for x in reversed(diffs):
        val = x[0] - val

    return val


if __name__ == '__main__':
    inp = read_input()
    #inp = SAMPLE_INPUT

    print(sum([solve_1(x) for x in inp]))
    print(sum([solve_2(x) for x in inp]))


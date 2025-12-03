"""Advent of Code 2024 - Day 2 Part 1"""
from pathlib import Path


INPUT_PATH = Path(__file__).parents[1].joinpath('input', 'day2.txt')


def valid_report(report: list[int], valid_seq: list[int]) -> bool:
    """Validate a report.

    Parameters
    ----------
    report: list of int
    valid_seq: list of int

    Returns
    -------
    bool
        True if report is valid, else False.
    """
    for i in range(len(report) - 1):
        if report[i+1] - report[i] not in valid_seq:
            return False

    return True


def parse_input() -> list[list[int]]:
    """Parse the input from a text file.

    Parameters
    ----------
    None.

    Returns
    -------
    list of list of int
    """
    return [
        [int(y) for y in x.split()]
        for x in  Path('input.txt').read_text().split('\n') if x
    ]


if __name__ == '__main__':
    num_valid = 0
    inc_seq = range(1, 4)
    dec_seq = range(-3, 0)

    for report in parse_input():
        if valid_report(report, inc_seq) or valid_report(report, dec_seq):
            num_valid += 1

    print(f'Day 02 Part 1 answer: {num_valid}')

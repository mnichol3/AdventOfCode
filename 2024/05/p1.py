"""Advent of Code 2024 - Day 5 Part 1"""
from collections import defaultdict
from pathlib import Path


def parse_input(fname: str = None) -> tuple[defaultdict, list[str]]:
    """Parse the input from a text file.

    Parameters
    ----------
    None.

    Returns
    -------
    defaultdict
        Set of rules, where each value is a set of numbers that the
        corresponding key must preceed.
    list of str
        Pages.
    """
    fname = 'input.txt' if fname is None else fname
    raw_inp = Path(fname).read_text().split('\n\n')

    rules = defaultdict(set)
    for x in raw_inp[0].split('\n'):
       a, b = x.split('|')
       rules[int(b)].add(int(a))

    updates = [y for y in raw_inp[1].split('\n') if y]

    return rules, updates


def part1(rules: defaultdict, pages: list[str]) -> int:
    sum = 0

    def count(row: list[str]) -> int:
        invalid = set()

        for r in row:
            if r in invalid:
                return 0

            invalid |= rules[r]

        return row[len(row)//2]

    for x in pages:
        page = list(map(int, x.split(',')))
        sum += count(page)

    return sum


if __name__ == '__main__':
    print(f'Day 05 Part 1 answer: {part1(*parse_input("input.txt"))}')

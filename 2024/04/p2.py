"""Advent of Code 2024 - Day 4 Part 2"""
from p1 import parse_input


def count_matches(puzzle, m, n):
    if puzzle[m][n] != 'A':
        return 0

    ul = puzzle[m-1][n-1]
    ur = puzzle[m-1][n+1]
    ll = puzzle[m+1][n-1]
    lr = puzzle[m+1][n+1]

    if sorted([ul, lr]) == sorted([ur, ll]) == ['M', 'S']:
        return 1

    return 0


def part2(puzzle: list[str]) -> int:
    n = 0

    for i in range(1, len(puzzle) - 1):
        for j in range(len(puzzle[i]) - 1):
            n += count_matches(puzzle, i, j)

    return n


if __name__ == '__main__':
    print(f'Day 04 Part 2 answer: {part2(parse_input())}')

"""Advent of Code 2024 - Day 5 Part 2"""
from collections import defaultdict

from p1 import parse_input


def part2(rules: defaultdict, pages: list[str]) -> int:
    sum = 0

    def count(row: list[str], reordered: bool = False) -> int:
        # Key: page; value: last valid index
        valid_index = dict()

        for i, r in enumerate(row):
            if r in valid_index:
                j = valid_index[r]
                swapped = row[:j] + [r] + row[j:i] + row[i+1:]
                return count(swapped, True)

            for val in rules[r]:
                if val not in valid_index:
                    valid_index[val] = i

        return row[len(row)//2] if reordered else 0

    for x in pages:
        page = list(map(int, x.split(',')))
        sum += count(page)

    return sum


if __name__ == '__main__':
    print(f'Day 05 Part 2 answer: {part2(*parse_input("input.txt"))}')

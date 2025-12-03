"""
Advent of Code 2023
Day 7 - Camel Cards
"""
from pathlib import Path


def read_input(file_path: Path) -> list[str]:
    """Read input file"""
    return file_path.read_text().splitlines()


def solve_1(hands: list[str]) -> float:
    """Part 1"""
    hands = ((
        max(map(hand.count, hand)),
        -len(set(hand)),
        *map('23456789TJQKA'.index, hand),
        int(bid),
        ) for hand, bid in map(str.split, hands))

    sum = 0
    for rank, (*_, bid) in enumerate(sorted(hands)):
        sum += (rank + 1) * bid

    return sum


def solve_2(hands: list[str]) -> float:
    """Part 2"""
    hands = ((
        max(map(hand.count, hand)),
        -len(set(hand)),
        *map('J23456789TQKA'.index, hand),
        int(bid),
        ) for hand, bid in map(str.split, hands))

    sum = 0
    for rank, (*_, bid) in enumerate(sorted(hands)):
        sum += (rank + 1) * bid

    return sum


if __name__ == '__main__':
    #result = solve_1(read_input(Path('input.txt')))
    result = solve_2(read_input(Path('input.txt')))
    print(result)
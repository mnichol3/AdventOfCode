"""Advent of Code 2024 - Day 22 Part 1"""
from pathlib import Path


def parse_input(f_path: str = 'input.txt') -> list[int]:
    return [int(x) for x in Path(f_path).read_text().split('\n') if x != '']


def step(n: int) -> int:
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216

    return n


if __name__ == '__main__':
    sum = 0

    for shopper in parse_input():
        for _ in range(2000):
            shopper = step(shopper)

        sum += shopper

    print(f'Part 1 answer: {sum}')

"""Advent of Code 2024 - Day 2 Part 2"""
from p1 import parse_input


def is_valid(seq: list[int], safe_range: range):
    for i in range(1, len(seq)):
        if seq[i] - seq[i-1] not in safe_range:
            return False
    return True


if __name__ == '__main__':
    num_valid = 0
    inc_seq = range(1, 4)
    dec_seq = range(-3, 0)

    for report in parse_input():
        num_valid += any(
            is_valid(report[:i] + report[i+1:], safe_range)
            for safe_range in (inc_seq, dec_seq)
            for i in range(len(report))
        )

    print(f'Day 02 Part 2 answer: {num_valid}')

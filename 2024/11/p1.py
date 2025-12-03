"""Advent of Code 2024 - Day 11 Part 1 & 2"""
import functools
import time
from collections import Counter
from pathlib import Path


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer


def parse_input(f_name: str = 'input.txt') -> str:
    """Parse the input from a text file.

    Parameters
    ----------
    fname: str, optional
        Input filename. Default is 'input.txt'.

    Returns
    -------
    str
    """
    return [x for x in Path(f_name).read_text().split('\n') if x][0]


@timer
def solution(stones: str) -> None:
    """Solution to Part 1 & 2.

    Parameters
    ----------
    stones: str
        String of stones.

    Returns
    -------
    None.
    """
    stones = Counter(map(int, stones.split()))

    for blink in range(1, 76):
        new_stones = Counter()

        for pebble, num_pebble in stones.items():
            if pebble == 0:
                new_stones[1] += num_pebble
            elif len(s := str(pebble)) % 2 == 0:
                for i in int(s[:len(s)//2]), int(s[len(s)//2:]):
                    new_stones[i] += num_pebble
            else:
                new_stones[pebble*2024] += num_pebble

        stones = new_stones

        if blink in (25, 75):
            print(sum(new_stones.values()))


if __name__ == '__main__':
    solution(parse_input())

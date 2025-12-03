"""Advent of Code 2024 - Day 22 Part 2"""
from collections import defaultdict

from p1 import parse_input, step


def get_prices(n: int) -> list[tuple[int, int]]:
    """Compute the prices and price changes."""
    prices = []

    for _ in range(2000):
        new_n = step(n)

        last_price = n % 10
        new_price = new_n % 10

        prices.append((new_price - last_price, new_price))

        n = new_n

    return prices


patterns = defaultdict(int)
for shopper in parse_input():
    added = set()
    prices = get_prices(shopper)

    for i in range(len(prices) - 3):
        p = tuple(d[0] for d in prices[i:i+4])
        if p in added:
            continue

        patterns[p] += prices[i+3][1]
        added.add(p)

print(f"part 2: {max(patterns.values())}")
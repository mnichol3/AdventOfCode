"""Advent of Code 2024 - Day 22 Part 1"""
from collections import defaultdict
from itertools import combinations


def parse_input(f_path: str = 'input.txt') -> dict:
    """Read input from a text file and return as a dictionary.

    Parameters
    ----------
    f_path: str, optional
        Input file path. Default is "input.txt."

    Returns
    -------
    dict
    """
    network = defaultdict(set)

    with open(f_path, 'r') as f:
        for line in f.read().splitlines():
            a, b = line.split('-')
            network[a].add(b)
            network[b].add(a)

    return network


def find_connections(network: dict) -> set:
    connections = set()
    for node in network:
        if node.startswith('t'):
            for c1, c2 in combinations(network[node], 2):
                if c1 in network[c2]:
                    # Sort tuple before adding to prevent tuples contining
                    # the same values in a different order from being added
                    connections.add(tuple(sorted([node, c1, c2])))

    return connections


if __name__ == '__main__':
    connections = find_connections(parse_input())
    print(f'Part 1 answer: {len(connections)}')

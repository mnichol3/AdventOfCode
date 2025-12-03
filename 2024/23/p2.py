"""Advent of Code 2024 - Day 22 Part 2"""
import networkx as nx


def init_graph(f_path: str = 'input.txt') -> nx.Graph:
    """Read input from a text file and return as a networkx Graph.

    Parameters
    ----------
    f_path: str, optional
        Input file path. Default is "input.txt."

    Returns
    -------
    networkx.Graph
    """
    g = nx.Graph()

    with open(f_path, 'r') as f:
        for line in f.read().splitlines():
            g.add_edge(*line.split('-'))

    return g


if __name__ == '__main__':
    network = init_graph()

    clusters = list(nx.find_cliques_recursive(network))
    clusters.sort(key=len, reverse=True)
    clusters[0].sort()

    print(f'Part 2 answer: {",".join(clusters[0])}')

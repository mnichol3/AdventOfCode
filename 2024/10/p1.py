"""Advent of Code 2024 - Day 10 Part 1"""
from __future__ import annotations
from pathlib import Path


class Node:
    """A node of a graph.

    Attributes
    ----------
    position: tuple of int, int
        Node x- and y- position.
    value: int
        Node value. In this case, it represents elevation.
    x: int
        Node x-position
    y: int
        Node y-position
    """

    def __init__(self, position: tuple[int, int], value: int) -> None:
        """Instantiate a Node.

        Parameters
        ----------
        position: tuple of int, int
            Node x- and y- position.
        value: int
            Elevation value.

        Returns
        -------
        None.
        """
        self.position = position
        self.value = value

    @property
    def x(self) -> int:
        """Return the Node's x-position."""
        return self.position[0]

    @property
    def y(self) -> int:
        """Return the Node's y-position."""
        return self.position[1]

    def is_valid_neighbor(self, node: Node) -> bool:
        """Determine if the given node is a valid neighbor.

        Parameters
        ----------
        node: Node
            Node to test.

        Returns
        -------
        bool
        """
        dx = abs(node.x - self.x)
        dy = abs(node.y - self.y)
        dv = node.value - self.value

        return (dx, dy) in [(0, 1), (1, 0)] and dv == 1

    def __eq__(self, node: Node) -> bool:
        """Determine if two nodes are equal."""
        return (
            node.x == self.x and
            node.y == self.y and
            node.value == self.value)

    def __hash__(self) -> int:
        """Return a hash of the Node."""
        return hash(self.position)

    def __repr__(self) -> str:
        """Return a string representation of the Node."""
        n = f'{self.position} value={self.value}'
        return (f'<{self.__class__.__qualname__} {n}>')


class Graph:
    """Class to loosely represent a Graph.

    Attributes
    ----------
    nodes: list of Node
        List of Nodes in the graph.
    roots: list of Node
        List of Nodes whose value is 0.
    num_nodes: int
        Number of nodes present in the graph.
    num_roots: int
        Number of roots present in the graph.
    """

    def __init__(self, matrix: list[list[int]]) -> None:
        """Instantiate a Graph.

        Parameters
        ----------
        matrix: list of list of int
            Elevation map to construct the graph for.

        Returns
        -------
        None.
        """
        self.nodes = []
        self.roots = []
        self._build(matrix)

    @property
    def num_roots(self) -> int:
        """Return the number of roots in the graph."""
        return len(self.roots)

    @property
    def num_nodes(self) -> int:
        """Return the number of nodes in the graph."""
        return len(self.nodes)

    def _build(self, matrix: list[list[int]]):
        """Populate the Graph's nodes and roots from the given matrix."""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr_node = Node((i, j), matrix[i][j])
                if curr_node.value == 0:
                    self.roots.append(curr_node)
                else:
                    self.nodes.append(curr_node)

    def get_neighbors(self, node: Node) -> list[Node]:
        """Return the neighbors of the given Node."""
        # TODO use adjacency matrix instead of this degeneracy
        return [x for x in self.nodes if node.is_valid_neighbor(x)]

    def part1(
        self,
        current_node: Node,
        visited: set[Node],
        endpoints: list[Node],
    ) -> list[Node]:
        """Solution for Part 1.
        Perform a depth-first search and return the number of endpoints reached.

        Parameters
        ----------
        current_node: Node
        visited: set of Node
        endpoints: list of Node

        Returns
        -------
        list of Node
        """
        if current_node not in visited:
            visited.add(current_node)

            if current_node.value == 9:
                endpoints.append(current_node)

            for neighbor in self.get_neighbors(current_node):
                self.part1(neighbor, visited, endpoints)

        return endpoints

    def part2(
        self,
        current_node: Node,
        visited: list[Node],
        paths: list[list[Node]],
    ) -> list[Node]:
        """Solution for Part 2.
        Perform a depth-first search and return the unique paths.

        Parameters
        ----------
        current_node: Node
        visited: list of Node
        paths: list of list of Node

        Returns
        -------
        list of list of Node
            Every unique path from the start node the terminus node.
        """
        if current_node not in visited:
            visited.append(current_node)

            for neighbor in self.get_neighbors(current_node):
                self.part2(neighbor, visited.copy(), paths)

        if visited[-1].value == 9:
            paths.append(visited)

        return paths

    def __repr__(self) -> str:
        """Return a string representation of the Graph."""
        return f'<{self.__class__.__qualname__}>'


def parse_input(f_name: str = 'input.txt') -> list[list[int]]:
    """Parse the input from a text file.

    Parameters
    ----------
    fname: str, optional
        Input filename. Default is 'input.txt'.

    Returns
    -------
    list of list of int
    """
    return [
        [int(y) for y in x]
        for x in Path(f_name).read_text().split('\n') if x
    ]


if __name__ == '__main__':
    graph = Graph(parse_input())

    sum = 0
    for start_node in graph.roots:
        sum += len(graph.part1(start_node, set(), []))

    print(f'Answer: {sum}')

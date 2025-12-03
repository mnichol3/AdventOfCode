
from p1 import Node, parse_input


def create_matrix(topo: list[list[int]]):
    """Create adjacency matrix."""
    ni = len(topo)
    nj = len(topo[0])

    def get_neighbors(i, j):
        neighbors = []
        for pos in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            ii = i + pos[0]
            jj = j + pos[1]

            if 0 <= ii < ni and 0 <= jj < nj:
                neighbors.append(Node((ii, jj), topo[ii][jj]))

        return neighbors

    roots = []
    matrix = {}

    for i in range(ni):
        for j in range(nj):
            curr_node = Node((i, j), topo[i][j])
            if curr_node.value == 0:
                roots.append(curr_node)

            matrix[curr_node] = [x for x in get_neighbors(i, j)
                                 if curr_node.is_valid_neighbor(x)]

    return matrix, roots


def part1(
    matrix: dict,
    current_node: Node,
    visited: set[Node],
    endpoints: list[Node],
) -> list[Node]:
    """Solution for Part 1.
    Perform a depth-first search and return the number of endpoints reached.

    Parameters
    ----------
    matrix: dict[Node, list[Node]]
    current_node: Node
    visited: set of Node
    endpoints: list of Node

    Returns
    -------
    list of Node
    """
    if current_node not in visited:
        visited.add(current_node)

        for neighbor in matrix[current_node]:
            part1(matrix, neighbor, visited, endpoints)

        if current_node.value == 9:
            endpoints.append(current_node)

    return endpoints


def part2(
    matrix: dict,
    current_node: Node,
    visited: list[Node],
    paths: list[list[Node]],
) -> list[Node]:
    """Solution for Part 2.
    Perform a depth-first search and return the unique paths.

    Parameters
    ----------
    matrix: dict[Node, list[Node]]
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

        for neighbor in matrix[current_node]:
            part2(matrix, neighbor, visited.copy(), paths)

    if visited[-1].value == 9:
        paths.append(visited)

    return paths


if __name__ == '__main__':
    graph, roots = create_matrix(parse_input())

    sum = 0
    for start_node in roots:
        sum += len(part1(graph, start_node, set(), []))

    print(f'Part1 answer: {sum}')

    sum = 0
    for start_node in roots:
        sum += len(part2(graph, start_node, [], []))

    print(f'Part2 answer: {sum}')

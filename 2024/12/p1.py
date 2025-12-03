"""Advent of Code 2024 - Day 12 Part 1"""
from pathlib import Path


def parse_input(f_name: str = 'input.txt') -> list[list[str]]:
    """Parse the input from a text file."""
    return [list(x) for x in Path(f_name).read_text().split('\n') if x]


valid_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def area(group: set | list) -> int:
    """Compute the area of a group."""
    return len(group)


def perimeter(group: set | list) -> int:
    """Compute the perimeter of a group."""
    p = 0

    for (i, j) in group:
        for (di, dj) in valid_moves:
            if (i+di, j+dj) not in group:
                p += 1

    return p


def bfs(
    garden: list[list[str]],
    curr_node: tuple[int, int],
) -> tuple[set, set]:
    """Breadth-first search."""
    group = set([curr_node])
    visited = set()
    ni = len(garden)
    nj = len(garden[0])
    i, j = curr_node
    curr_val = garden[i][j]
    curr = [curr_node]

    while curr:
        to_visit = []

        for (i, j) in curr:
            for (di, dj) in valid_moves:
                ii = i + di
                jj = j + dj

                if (
                    0 <= ii < ni and
                    0 <= jj < nj and
                    garden[ii][jj] == curr_val and
                    (ii, jj) not in visited
                ):
                    visited.add((ii, jj))
                    group.add((ii, jj))
                    to_visit.append((ii, jj))

            curr = to_visit

    return group, visited


def part1(garden: list[list[str]]) -> int:
    sum = 0
    visited = set()

    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) in visited:
                continue

            group, just_visited = bfs(garden, (i, j))

            visited |= just_visited

            curr_area = area(group)
            curr_perim = perimeter(group)

            sum += curr_area * curr_perim

    return sum


if __name__ == '__main__':
    print(part1(parse_input()))

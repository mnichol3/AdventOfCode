"""Advent of Code 2024 - Day 12 Part 1 & 2"""
from __future__ import annotations
from enum import Enum
from pathlib import Path


class Move(Enum):
    UP = (-1, 0)
    LEFT = (0, -1)
    DOWN = (1, 0)
    RIGHT = (0, 1)

    @classmethod
    def clockwise(cls) -> list[Move]:
        return [cls.UP, cls.RIGHT, cls.DOWN, cls.LEFT]

    def __radd__(self, loc: tuple[int, int]) -> tuple[int, int]:
        return loc[0] + self.value[0], loc[1] + self.value[1]


class Garden:

    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.ni = len(grid)
        self.nj = len(grid[0])

    def bfs(self, node: tuple[int, int]) -> tuple[set, set]:
        group = set([node])
        visited = set()
        i, j = node
        curr_val = self.get(node)
        curr = [node]

        while curr:
            to_visit = []
            for (i, j) in curr:
                for move in Move:
                    (ii, jj) = (i, j) + move
                    if (
                        self.get((ii, jj)) == curr_val and
                        (ii, jj) not in visited
                    ):
                        visited.add((ii, jj))
                        group.add((ii, jj))
                        to_visit.append((ii, jj))

                curr = to_visit

        return group, visited

    def contains(self, loc: tuple[int, int]) -> bool:
        return 0 <= loc[0] < self.ni and 0 <= loc[1] < self.nj

    def get(self, loc: tuple[int, int]) -> int:
        if not self.contains(loc):
            return None
        return self.grid[loc[0]][loc[1]]

    @classmethod
    def from_file(cls, f_path: str | Path = 'input.txt') -> Garden:
        return cls(
            [list(x)for x in Path(f_path).read_text().split('\n') if x])

    def __repr__(self):
        return f'<{self.__class__.__qualname__} {self.ni}x{self.nj}>'


def calc_area(group: set | list) -> int:
    """Compute the area of a group."""
    return len(group)


def calc_perimeter(group: set | list) -> int:
    """Compute the perimeter of a group."""
    p = 0

    for g in group:
        for move in Move:
            if g + move not in group:
                p += 1

    return p


def calc_sides(garden: Garden, group: set | list, val: str) -> int:

    def count_edges(node: tuple[int, int], val: str) -> int:
        diagonals = {
            'UP': (-1, 1),
            'RIGHT': (1, 1),
            'DOWN': (1, -1),
            'LEFT': (-1, -1),
        }

        n = 0
        moves = Move.clockwise()
        moves += [moves[0]]

        for i, move in enumerate(moves[:-1]):
            if (
                garden.get(node + move) != val and
                garden.get(node + moves[i+1]) != val
            ):
                n += 1

            elif (
                garden.get(node + move) == val and
                garden.get(node + moves[i+1]) == val
            ):
                garden.get(node + diagonals[move.name]) != val
                diag = diagonals[move.name]

                if garden.get((node[0]+diag[0], node[1]+diag[1])) != val:
                    n += 1

        return n

    if len(group) in [1, 2]:
        return 4

    sides = 0
    for node in group:
        sides += count_edges(node, val)

    return sides


def solution(garden: Garden) -> int:
    p1 = 0
    p2 = 0
    visited = set()

    for i in range(garden.ni):
        for j in range(garden.nj):
            if (i, j) in visited:
                continue

            curr_group, just_visited = garden.bfs((i, j))
            curr_val = garden.get((i, j))

            visited |= just_visited

            area = calc_area(curr_group)
            perim = calc_perimeter(curr_group)
            n_sides = calc_sides(garden, curr_group, curr_val)

            p1 += area * perim
            p2 += area * n_sides

    return p1, p2


if __name__ == '__main__':
    ans1, ans2 = solution(Garden.from_file())
    print(f'Part 1 answer: {ans1}')
    print(f'Part 2 answer: {ans2}')

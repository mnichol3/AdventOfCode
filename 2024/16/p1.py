"""Advent of Code 2024 - Day 16 Part 1"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from operator import sub
from pathlib import Path
from queue import PriorityQueue


Point = tuple[int, int]


def parse_input(f_path: str = 'input.txt') -> any:
    return [list(x) for x in Path(f_path).read_text().split('\n') if x]


def subtract(a: Point, b: Point) -> Point:
    return tuple(map(sub, a, b))


def update_cost(reindeer: Reindeer, pos: Point):
    result = reindeer.cost
    if subtract(pos, reindeer.pos) != reindeer.direction:
        result += 1000

    return result + 1


class Move(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)


@dataclass
class Reindeer:
    pos: tuple
    cost: int
    direction: tuple
    visited: set

    def __hash__(self):
        return hash((self.pos, self.cost, self.direction))

    def __repr__(self):
        return f'<Reindeer ({self.pos}, {self.cost}, {self.direction})>'

    def __lt__(self, other):
        return self.cost < other.cost


class Solution:

    def __init__(self, maze: list[list[str]]) -> None:
        self.maze = maze
        self.ni = len(maze)
        self.nj = len(maze[0])

    def _get_start_end(self) -> tuple[int, int]:
        start = None
        end = None
        for i in range(self.ni):
            for j in range(self.nj):
                if self.maze[i][j] == 'S':
                    start = (i, j)
                elif self.maze[i][j] == 'E':
                    end = (i, j)
                    self.maze[i][j] = '.'

            if start and end:
                return start, end

    def get_neighbors(self, pos: Point) -> list[Point]:
        """Maze is bounded by #, so we dont need to check fot out-of-bounds."""
        neighbors = []
        i, j = pos
        for move in Move:
            di, dj = move.value
            ii = i + di
            jj = j + dj

            if self.maze[ii][jj] == '.':
                neighbors.append((ii, jj))

        return neighbors

    def solve(self) -> int:
        result = []

        start, end = self._get_start_end()

        q = PriorityQueue()
        q.put(Reindeer(start, 0, Move.EAST.value, set()))

        min_cost = float('inf')
        junction_lowest = {}

        while not q.empty():
            reindeer = q.get()
            neighbors = self.get_neighbors(reindeer.pos)

            if reindeer.cost > min_cost:
                continue

            if len(neighbors) > 1:
                least = junction_lowest.get(reindeer.pos)
                if least is not None and least < reindeer.cost:
                    continue

                junction_lowest[reindeer.pos] = reindeer.cost

            for n in neighbors:
                if n == end:
                    result.append(update_cost(reindeer, n))
                elif n not in reindeer.visited:
                    visited2 = reindeer.visited.copy()
                    visited2.add(n)
                    cost2 = update_cost(reindeer, n)

                    if len(result) == 0 or cost2 < min(result):
                        q.put(
                            Reindeer(n, cost2,
                                     subtract(n, reindeer.pos), visited2))

        return min(result)

    def draw(self, shortest_path: list[tuple[int, int]]) -> None:
        for p in shortest_path[1:-1]:
            self.maze[p[0]][p[1]] = 'O'

        start = shortest_path[0]
        self.maze[start[0]][start[1]] = 'S'

        end = shortest_path[-1]
        self.maze[end[0]][end[1]] = 'E'

        for x in self.maze:
            print(''.join(x))


if __name__ == '__main__':
    soln = Solution(parse_input())
    print(f"Part 1 answer: {soln.solve()}")

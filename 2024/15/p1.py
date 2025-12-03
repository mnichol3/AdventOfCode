"""Advent of Code 2024 - Day 15 Part 1"""
from __future__ import annotations
from pathlib import Path


def parse_input(f_path: str = 'input.txt') -> tuple:
    inp = Path(f_path).read_text().split('\n\n')
    return [list(x) for x in inp[0].split('\n')], inp[1].replace('\n', '')


MoveDirs = {
    '^': (-1, 0),
    '<': (0, -1),
    'v': (1, 0),
    '>': (0, 1),
}


class Fishtank:

    def __init__(self, tank_map: list[list[str]]) -> None:
        self.grid = tank_map
        self.num_i, self.num_j = self._set_dims()
        self.robot_pos = self._get_init_pos()
        self.part = 1

    def _get_init_pos(self) -> tuple[int, int]:
        """Find edges and robot's initial position"""
        rpos = None
        for i in range(self.num_i):
            for j in range(self.num_j):
                if self.grid[i][j] == '@':
                    rpos = (i, j)
                    self.grid[i][j] = '.'
                    break

        return rpos

    def _set_dims(self) -> tuple[int, int]:
        return len(self.grid), len(self.grid[0])

    def move_robot(self, move_str: str) -> tuple[int, int]:
        i, j = self.robot_pos
        di, dj = MoveDirs[move_str]

        ii = i + di
        jj = j + dj

        if self.grid[ii][jj] == '.':
            self.robot_pos = (ii, jj)
        elif self.grid[ii][jj] == '#':
            return
        else:
            edges, adjacent = self._get_adjacent(i, j, move_str)
            blocked = 0
            di, dj = MoveDirs[move_str]
            for box in edges:
                ni = box[0] + di
                nj = box[1] + dj
                if self.grid[ni][nj] == "#":
                    blocked += 1
            if blocked == 0:
                self.update_grid(adjacent, move_str)
                self.robot_pos = (i + di, j + dj)

    def update_grid(self, adjacent: list[tuple], move_str: str) -> None:
        coords = []

        if move_str == '^':
            coords = sorted(adjacent, key=lambda x : x[0])
        elif move_str == 'v':
            coords = sorted(adjacent, key=lambda x : x[0], reverse=True)
        elif move_str == '>':
            coords = sorted(adjacent, key=lambda x : x[1], reverse=True)
        elif move_str == '<':
            coords = sorted(adjacent, key=lambda x : x[1])

        di, dj = MoveDirs[move_str]
        for c in coords:
            i, j = c
            ni = i + di
            nj = j + dj
            self.grid[ni][nj] = self.grid[i][j]
            self.grid[i][j] = '.'

    def _get_adjacent(self, i: int, j: int, move_str: str) -> any:
        adj = set()
        di, dj = MoveDirs[move_str]
        orig_i = i
        orig_j = j

        if self.part == 1 or move_str in '<>':
            while True:
                ni = i + di
                nj = j + dj

                if self.grid[ni][nj] in '.#':
                    return [(ni-di, nj-dj)], adj

                i = ni
                j = nj
                adj.add((i, j))
        else:
            edges = []
            queue = [(i, j)]

            while queue:
                i, j = queue.pop(0)

                if (i, j) in adj:
                    continue

                adj.add((i, j))
                ni = i + di
                nj = j + dj

                if self.grid[ni][nj] in '.#':
                    edges.append((i, j))
                elif self.grid[ni][nj] == '[':
                    queue.append((ni, nj))
                    queue.append((ni, nj+1))
                elif self.grid[ni][nj] == ']':
                    queue.append((ni, nj))
                    queue.append((ni, nj-1))

            return edges, adj - {(orig_i, orig_j)}


def part1(f_path: str = 'input.txt') -> int:
    """Solution to Part 1."""
    tank_map, moves = parse_input(f_path)
    fishtank = Fishtank(tank_map)

    for m in moves:
        fishtank.move_robot(m)

    return sum(
        100 * i + j for i in range(fishtank.num_i)
        for j in range(fishtank.num_j) if fishtank.grid[i][j] == 'O')


if __name__ == '__main__':
    print(f'Part 1 answer: {part1()}')

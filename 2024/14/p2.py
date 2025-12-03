"""Advent of Code 2024 - Day 14 Part 2"""
import math
from itertools import combinations
from p1 import parse_input


class Robot:

    def __init__(
        self,
        position: tuple[int, int],
        velocity: tuple[int, int],
    ) -> None:
        self.position = position
        self.velocity = velocity

    @property
    def x(self) -> int:
        return self.position[0]

    @property
    def y(self) -> int:
        return self.position[1]

    @property
    def vx(self) -> int:
        return self.velocity[0]

    @property
    def vy(self) -> int:
        return self.velocity[1]

    def move(self, nx: int, ny: int, t: int = 1) -> None:
        x = (self.x + self.vx*t) % nx
        y = (self.y + self.vy*t) % ny

        self.position = (x, y)

    def __repr__(self) -> str:
        return f'<{self.__class__.__qualname__} {self.position}>'


def part2() -> int:
    """Solution to Part 2.

    Find the timestep corresponding to the minimum average distance
    between all robots. Not very efficient, but works.
    """

    def dist(p1, p2):
        (x1, y1), (x2, y2) = p1, p2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    nx = 101
    ny = 103
    nt = int(10e3)

    min_dist = 10e5
    min_idx = 0

    robots = []
    for x in parse_input():
        robots.append(Robot(*x))

    for t in range(nt):
        points = []
        for i in range(len(robots)):
            robots[i].move(nx, ny)
            points.append(robots[i].position)

        d_list = [dist(p1, p2) for p1, p2 in combinations(points, 2)]
        curr_dist = sum(d_list) / len(d_list)

        if curr_dist < min_dist:
            min_dist = curr_dist
            min_idx = t + 1

    return min_idx


if __name__ == '__main__':
    print(f'Part 2 answer: {part2()}')

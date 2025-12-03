"""Advent of Code 2024 - Day 20 Part 1"""
from collections import deque
from enum import Enum
from pathlib import Path


Point = tuple[int, int]


def parse_input(f_path = 'input.txt') -> list[list[str]]:
    """Parse input from file.

    Parameters
    ----------
    f_path: str, optional
        Input file path. Default is 'input.txt'.

    Returns
    -------
    list of list of str
    """
    return [list(x) for x in Path(f_path).read_text().split('\n') if x]


class Move(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class Maze:

    def __init__(self, input: list[list[str]]) -> None:
        self.map = input
        self.ni = len(input)
        self.nj = len(input[0])
        self.start, self.end = self.get_start_end()

    def bfs(self) -> list[Point]:
        """BFS returning the shorted path between the start & end points."""
        visited = {}
        queue = deque()

        (i, j) , end_pos = self.start, self.end

        visited[(i, j)] = None
        queue.append((i, j))

        while queue:
            (i, j) = queue.popleft()

            if (i, j) == end_pos:
                path = []
                curr_pos = (i, j)
                while curr_pos:
                    path.append(curr_pos)
                    curr_pos = visited[curr_pos]
                return path[::-1]

            for move in Move:
                di, dj = move.value
                ii = i + di
                jj = j + dj

                if self._valid_move((ii, jj)) and (ii, jj) not in visited:
                    visited[(ii, jj)] = (i, j)
                    queue.append((ii, jj))

    def get_start_end(self) -> tuple[Point]:
        """Get the coordinates of the start & end positions."""
        start = None
        end = None

        for i in range(self.ni):
            for j in range(self.nj):
                if self.map[i][j] == 'S':
                    start = (i, j)
                elif self.map[i][j] == 'E':
                    end = (i, j)

                if start and end:
                    break

        return start, end

    def print(self, path: list[Point] = None) -> None:
        """Print the maze."""
        maze = self.map.copy()

        if path:
            for (i, j) in path:
                maze[i][j] = 'O'

            maze[self.start[0]][self.start[1]] = 'S'
            maze[self.end[0]][self.end[1]] = 'E'

        for row in maze:
            print(''.join(row))

    def _valid_move(self, next_pos: Point) -> bool:
        ii, jj = next_pos

        if (
            0 <= ii < self.ni and 0 <= jj < self.nj and
            self.map[ii][jj] != '#'
        ):
            return True

        return False


def calc_distance(a: Point, b: Point) -> int:
    """Calculate the manhattan distance between two points."""
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def diff(a: Point, b: Point) -> tuple[int, int]:
        """Get the i & j deltas between two points."""
        return (a[0]-b[0], a[1]-b[1])


def point_between(a: Point, b: Point) -> Point:
        """Get the coordinates of the point between point a and point b."""
        di = (b[0] - a[0]) // 2
        dj = (b[1] - a[1]) // 2

        return (a[0]+di, a[1]+dj)


def find_shortcuts(maze: Maze, best_path: list[Point]) -> any:
    """Find possible shortcuts in the best path.

    Logic:
        1. Identify points in the best path that have a distance of 2.
        2. Validate the point pair
            i. We haven't already visited point1
            ii. We aren't looping back to the start point.
        3. If the point between the point pair is an obstruction, find the
           distance between the point pair.
        3. Add the distance saved to a dictionary for outputting.

    Parameters
    ----------
    maze: Maze
        Maze.
    best_path: list of tuple of (int, int)
        Coordinates of the computed best path.
    """
    shortcuts = {}
    visited = set()

    for idx, point1 in enumerate(best_path):
        for point2 in best_path[idx+3:]:
            if point2 == maze.start:
                continue

            if calc_distance(point1, point2) == 2 and point2 not in visited:
                pi, pj = point_between(point1, point2)
                if maze.map[pi][pj] == '#':
                    len_saved = best_path.index(point2) \
                                - best_path.index(point1) - 2

                    if len_saved in shortcuts:
                        shortcuts[len_saved] += 1
                    else:
                        shortcuts[len_saved] = 1

        visited.add(point1)

    return shortcuts


if __name__ == '__main__':
    maze = Maze(parse_input())
    path = maze.bfs()
    print(f'Best path length = {len(path)-1}')

    shortcuts = find_shortcuts(maze, path)

    sum = 0
    for k, v in shortcuts.items():
        if k >= 100:
            sum += v

    print(f'Part 1 answer: {sum}')
